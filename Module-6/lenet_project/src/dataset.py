import torch
from torchvision import datasets, transforms
from torch.utils.data import Dataset, DataLoader
import os
import pandas as pd
from PIL import Image
from tqdm import tqdm
import requests

class CassavaDataset(Dataset):
    def __init__(self, root_dir, transform=None, train=True):
        self.root_dir = root_dir
        self.transform = transform
        self.train = train
        
        # Download dataset if not exists
        self._download_dataset()
        
        # Load labels
        csv_path = os.path.join(root_dir, 'train.csv' if train else 'test.csv')
        self.data = pd.read_csv(csv_path)
        self.img_dir = os.path.join(root_dir, 'train_images' if train else 'test_images')
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        img_name = self.data.iloc[idx]['image_id']
        img_path = os.path.join(self.img_dir, img_name)
        image = Image.open(img_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
            
        if self.train:
            label = self.data.iloc[idx]['label']
            return image, label
        return image
    
    def _download_dataset(self):
        # This is a placeholder. In real implementation, you would download from Kaggle API
        # For this example, we assume the data is already downloaded
        pass

def get_mnist_loaders(batch_size=32):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST('./data', train=False, transform=transform)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader

def get_cassava_loaders(batch_size=32):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    train_dataset = CassavaDataset(root_dir='./data/cassava', transform=transform, train=True)
    test_dataset = CassavaDataset(root_dir='./data/cassava', transform=transform, train=False)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    return train_loader, test_loader 