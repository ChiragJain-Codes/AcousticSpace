# AcousticSpace

An AI-powered Deepfake Audio Detection system built using **Python, FastAPI, Librosa, and Deep Learning (CNN)**.

This project is being developed as part of my internship and aims to detect whether an uploaded audio file is a **real human voice (bonafide)** or an **AI-generated/spoofed voice**.

---

# Features

- Audio Upload API using FastAPI
- Audio Processing with Librosa
- Waveform Generation
- Mel Spectrogram Generation
- MFCC Feature Extraction
- Automatic Dataset Organization
- Deepfake Audio Dataset Support
- CNN Model Training (In Progress)
- Real vs Fake Audio Prediction (Upcoming)

---

# Tech Stack

- Python 3.13
- FastAPI
- Librosa
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow / Keras (Upcoming)

---

# Project Structure

```
AcousticSpace/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── main.py
│   │   ├── organize_dataset.py
│   │   ├── dataset_loader.py
│   │   ├── dataset_preprocessor.py
│   │   └── ...
│   │
│   ├── uploads/
│   ├── requirements.txt
│   └── venv/
│
├── dataset/
│   ├── real/
│   └── fake/
│
├── README.md
└── .gitignore
```

---

# Dataset

This project uses the **official ASVspoof 2019 Logical Access (LA)** dataset.

## Official Source

https://datashare.ed.ac.uk/handle/10283/3336

Download:

```
LA.zip
```

---

## Why is the dataset not included?

The dataset is several gigabytes in size.

For this reason, it is intentionally excluded from the GitHub repository using `.gitignore`.

Only the source code is version controlled.

---

# Dataset Setup

## Step 1

Download the official dataset from:

https://datashare.ed.ac.uk/handle/10283/3336

---

## Step 2

Extract the dataset.

---

## Step 3

Update the paths inside:

```
backend/app/organize_dataset.py
```

if necessary.

---

## Step 4

Run

```bash
python organize_dataset.py
```

This script automatically creates

```
dataset/
│
├── real/
└── fake/
```

by reading the official protocol files and copying the corresponding audio files.

No manual organization is required.

---

# Current Development Progress

## Completed

- FastAPI Backend
- Audio Upload API
- Librosa Integration
- Audio Loading
- Waveform Visualization
- Mel Spectrogram Generation
- MFCC Feature Extraction
- Dataset Loader
- Dataset Preprocessor
- Automatic Dataset Organizer
- Official ASVspoof 2019 Dataset Integration

---

## In Progress

- RIR Feature Extraction
- Feature Fusion
- CNN Model
- Training Pipeline
- Evaluation
- Prediction API

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd AcousticSpace
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

# Current Workflow

```
Audio Upload
      │
      ▼
Librosa
      │
      ▼
Feature Extraction
      │
      ▼
MFCC
      │
      ▼
Dataset Preparation
      │
      ▼
CNN Training
      │
      ▼
Prediction
```

---

# Git Ignore

The following files are intentionally excluded from GitHub.

- dataset/
- backend/uploads/
- models/
- *.h5
- *.pth
- *.pt
- __pycache__/
- venv/

---

# Future Improvements

- RIR Features
- CNN Optimization
- Attention Mechanism
- Real-time Audio Detection
- Model Deployment
- Docker Support
- Cloud Deployment

---

# License

This project is developed for educational and internship purposes.

The ASVspoof 2019 dataset remains subject to its own license and terms of use.

---

# Author

**Chirag Jain**

Computer Science Engineering Student

AI | Machine Learning | Deep Learning | FastAPI | Python