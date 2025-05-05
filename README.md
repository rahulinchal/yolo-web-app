# YOLO Model Training and Inference Web Application

This web application enables users to train and use object detection models based on YOLO (You Only Look Once) frameworks. The app supports project setup, dataset uploads, model configuration, training, prediction, and multiple task types including Detection, Classification, and Segmentation.

# View Results
- To see the live results of this project, visit [Fitness Website Demo](https://rahulinchal.github.io/yolo-web-app/).
  
## Features

- **Project Management**: Create and organize projects with customizable names and descriptions
- **Multiple Task Types**: Support for Detection, Classification, and Segmentation
- **YOLO Version Selection**: Choose from YOLO v5, v6, v7, v8, and v11
- **Dataset Management**: Upload and organize images and annotations
- **Model Training**: Configure and train models with customizable parameters
- **Inference**: Make predictions on new images and visualize results
- **Result Storage**: Automatic organization of models, results, and metrics

## Installation

### Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (recommended for training)
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/rahulinchal/yolo-web-app.git
cd yolo-web-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download pre-trained weights (optional):
```bash
python download_weights.py
```

5. Start the application:
```bash
python app.py
```

6. Access the web interface at http://localhost:5000

## Dependencies

### Core Libraries
- Flask==2.0.1
- PyTorch==1.10.0
- torchvision==0.11.1
- ultralytics==8.0.0
- numpy==1.21.3
- Pillow==8.4.0
- matplotlib==3.4.3
- opencv-python==4.5.4.60
- pandas==1.3.4

### YOLO Dependencies
- yolov5==6.2.3
- yolov7-package==0.3.0
- yolov8==0.6.0

### Web Interface
- Flask-WTF==1.0.0
- Flask-Bootstrap==3.3.7.1
- Flask-SocketIO==5.1.1
- WTForms==3.0.0

## Usage Guide

### 1. Creating a New Project

1. Navigate to the main page and click "Create New Project"
2. Enter a project name and optional description
3. Select a task type (Detection, Classification, or Segmentation)
4. Click "Create Project"

### 2. Uploading Datasets

1. Select your project from the dashboard
2. Navigate to the "Dataset" tab
3. Upload your images and corresponding annotations:
   - For Detection: Images + YOLO format annotation files (.txt)
   - For Classification: Images organized in class folders
   - For Segmentation: Images + mask files

### 3. Training a Model

1. Navigate to the "Training" tab in your project
2. Select a YOLO version (v5, v6, v7, v8, or v11)
3. Configure training parameters:
   - Number of epochs
   - Batch size
   - Learning rate
   - Image size
4. Click "Start Training"
5. Monitor training progress and results

### 4. Running Predictions

1. Navigate to the "Prediction" tab
2. Upload new images or select from test set
3. Select a trained model
4. Click "Run Prediction"
5. View and download results

## Sample Datasets

See the `/sample_datasets` directory for examples of properly formatted datasets for each task type.

## Troubleshooting

- **CUDA errors**: Ensure you have compatible NVIDIA drivers installed
- **Memory issues**: Reduce batch size or image dimensions for training
- **Dataset format errors**: Check sample datasets for correct formatting

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The YOLOv5 implementation is based on [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- Additional YOLO versions are based on their respective repositories
