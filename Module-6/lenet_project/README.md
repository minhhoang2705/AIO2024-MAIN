# LeNet CNN for MNIST and Cassava Leaf Disease Classification

This project implements LeNet CNN architecture for both MNIST digit classification and Cassava Leaf Disease classification using PyTorch. It includes a web interface built with Streamlit for model inference.

## Project Structure
```
lenet_project/
├── data/               # Dataset storage
├── models/             # Trained model storage
├── src/               
│   ├── model.py       # LeNet model architecture
│   ├── dataset.py     # Dataset handling
│   ├── train.py       # Training script
│   └── app.py         # Streamlit web interface
├── static/            # Static files for web interface
└── requirements.txt   # Project dependencies
```

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Training

To train the model on MNIST dataset:
```bash
python src/train.py --dataset mnist --epochs 10 --batch_size 64
```

To train on Cassava Leaf Disease dataset:
```bash
python src/train.py --dataset cassava --epochs 10 --batch_size 64
```

Note: For the Cassava dataset, you need to download it from Kaggle and place it in the `data/cassava` directory with the following structure:
```
data/cassava/
├── train.csv
├── train_images/
└── test_images/
```

## Web Interface

To run the Streamlit web interface:
```bash
streamlit run src/app.py
```

The interface allows you to:
1. Select the dataset type (MNIST or Cassava)
2. Upload an image
3. View the model's prediction and class probabilities

## GPU Support

The code automatically uses GPU if available through PyTorch's `device` selection. No additional configuration is needed.

## Model Architecture

The LeNet architecture consists of:
- 2 Convolutional layers
- 2 Max pooling layers
- 3 Fully connected layers
- ReLU activation functions

The model is adapted to handle both grayscale (MNIST) and RGB (Cassava) images. 