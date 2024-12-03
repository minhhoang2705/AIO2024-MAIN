import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import io
from model import LeNet
import numpy as np

def load_model(model_path, num_classes, input_channels):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = LeNet(num_classes=num_classes, input_channels=input_channels)
    
    # Load checkpoint dictionary
    checkpoint = torch.load(model_path, map_location=device)
    
    # Extract model state dict from checkpoint
    if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
        model.load_state_dict(checkpoint['model_state_dict'])
    else:
        # Fallback for older saved models that might be just state_dict
        model.load_state_dict(checkpoint)
    
    model.to(device)
    model.eval()
    return model, device

def preprocess_image(image, dataset_type):
    if dataset_type == 'mnist':
        transform = transforms.Compose([
            transforms.Grayscale(),
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
    else:  # cassava
        transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    
    return transform(image).unsqueeze(0)

def main():
    st.title('LeNet Model Inference')
    
    # Model selection
    dataset_type = st.selectbox('Select Dataset', ['mnist', 'cassava'])
    
    if dataset_type == 'mnist':
        model_path = 'models/lenet_mnist.pth'
        num_classes = 10
        input_channels = 1
        class_names = [str(i) for i in range(10)]
    else:
        model_path = 'models/lenet_cassava.pth'
        num_classes = 5
        input_channels = 3
        class_names = ['CBB', 'CBSD', 'CGM', 'CMD', 'Healthy']
    
    try:
        model, device = load_model(model_path, num_classes, input_channels)
        st.success('Model loaded successfully!')
    except Exception as e:
        st.error(f'Error loading model: {str(e)}')
        st.info('Please make sure you have trained the model first.')
        return
    
    # File uploader
    uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Make prediction
        try:
            input_tensor = preprocess_image(image, dataset_type).to(device)
            
            with torch.no_grad():
                output = model(input_tensor)
                probabilities = torch.nn.functional.softmax(output, dim=1)[0]
                predicted_class = torch.argmax(probabilities).item()
            
            # Display results
            st.write('### Prediction Results')
            st.write(f'Predicted Class: {class_names[predicted_class]}')
            
            # Display probability distribution
            st.write('### Class Probabilities')
            probs_dict = {class_names[i]: float(probabilities[i]) * 100 for i in range(len(class_names))}
            
            # Create bar chart
            st.bar_chart(probs_dict)
            
        except Exception as e:
            st.error(f'Error during prediction: {str(e)}')

if __name__ == '__main__':
    main() 