import torch
import torch.nn as nn
import torch.optim as optim
from model import LeNet
from dataset import get_mnist_loaders, get_cassava_loaders
import os
from tqdm import tqdm
import argparse
from torch.optim.lr_scheduler import ReduceLROnPlateau
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, test_loader, criterion, device, class_names=None):
    model.eval()
    test_loss = 0
    correct = 0
    total = 0
    all_preds = []
    all_labels = []
    
    with torch.no_grad():
        for inputs, labels in tqdm(test_loader, desc='Evaluating'):
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
            
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    accuracy = 100. * correct / total
    avg_loss = test_loss / len(test_loader)
    
    # Generate detailed metrics
    print('\nTest Results:')
    print(f'Average Loss: {avg_loss:.4f}')
    print(f'Accuracy: {accuracy:.2f}%')
    
    if class_names:
        # Print classification report
        print('\nClassification Report:')
        print(classification_report(all_labels, all_preds, target_names=class_names))
        
        # Generate confusion matrix
        cm = confusion_matrix(all_labels, all_preds)
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                   xticklabels=class_names,
                   yticklabels=class_names)
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        plt.savefig('confusion_matrix.png')
        plt.close()
    
    return accuracy, avg_loss

def train_model(model, train_loader, test_loader, criterion, optimizer, scheduler, num_epochs, device, save_path, class_names=None):
    best_acc = 0.0
    train_losses = []
    val_accuracies = []
    patience = 5
    patience_counter = 0
    
    for epoch in range(num_epochs):
        # Training phase
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        progress_bar = tqdm(train_loader, desc=f'Epoch {epoch+1}/{num_epochs}')
        for inputs, labels in progress_bar:
            inputs, labels = inputs.to(device), labels.to(device)
            
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            
            # Gradient clipping to prevent exploding gradients
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            
            optimizer.step()
            
            running_loss += loss.item()
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
            
            progress_bar.set_postfix({
                'loss': f'{running_loss/len(train_loader):.3f}',
                'acc': f'{100.*correct/total:.2f}%'
            })
        
        train_losses.append(running_loss/len(train_loader))
        
        # Validation phase
        val_acc, val_loss = evaluate_model(model, test_loader, criterion, device)
        val_accuracies.append(val_acc)
        
        # Learning rate scheduling
        scheduler.step(val_loss)
        
        print(f'Epoch {epoch+1}/{num_epochs}:')
        print(f'Training Loss: {train_losses[-1]:.4f}')
        print(f'Validation Accuracy: {val_acc:.2f}%')
        print(f'Current Learning Rate: {optimizer.param_groups[0]["lr"]:.6f}')
        
        # Save best model
        if val_acc > best_acc:
            best_acc = val_acc
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'scheduler_state_dict': scheduler.state_dict(),
                'best_acc': best_acc,
            }, save_path)
            patience_counter = 0
        else:
            patience_counter += 1
        
        # Early stopping
        if patience_counter >= patience:
            print(f'\nEarly stopping triggered after {epoch+1} epochs')
            break
    
    # Plot training curves
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(train_losses)
    plt.title('Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    
    plt.subplot(1, 2, 2)
    plt.plot(val_accuracies)
    plt.title('Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    
    plt.tight_layout()
    plt.savefig('training_curves.png')
    plt.close()
    
    # Load best model and perform final evaluation
    checkpoint = torch.load(save_path)
    model.load_state_dict(checkpoint['model_state_dict'])
    print('\nPerforming final evaluation on best model:')
    evaluate_model(model, test_loader, criterion, device, class_names)
    
    return model, best_acc

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, choices=['mnist', 'cassava'], required=True)
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--lr', type=float, default=0.001)
    parser.add_argument('--weight_decay', type=float, default=1e-5)
    args = parser.parse_args()
    
    # Set device and enable cuDNN benchmarking
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True
    print(f'Using device: {device}')
    
    # Get data loaders
    if args.dataset == 'mnist':
        train_loader, test_loader = get_mnist_loaders(args.batch_size)
        model = LeNet(num_classes=10, input_channels=1).to(device)
        save_path = 'models/lenet_mnist.pth'
        class_names = [str(i) for i in range(10)]
    else:
        train_loader, test_loader = get_cassava_loaders(args.batch_size)
        model = LeNet(num_classes=5, input_channels=3).to(device)
        save_path = 'models/lenet_cassava.pth'
        class_names = ['CBB', 'CBSD', 'CGM', 'CMD', 'Healthy']
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=3, verbose=True)
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Train the model
    model, best_acc = train_model(model, train_loader, test_loader, criterion, optimizer, 
                                 scheduler, args.epochs, device, save_path, class_names)
    
    print(f'\nTraining completed! Best validation accuracy: {best_acc:.2f}%')

if __name__ == '__main__':
    main() 