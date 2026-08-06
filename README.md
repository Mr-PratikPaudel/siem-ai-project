# AI-Powered SIEM - Machine Learning Module


Download link for csv files:https://drive.google.com/drive/folders/1L-aduCw5j2Py3L1gpZr9v5s3eKKcx3T7?usp=drive_link

An AI-powered Security Information and Event Management (SIEM) system that detects anomalous network traffic using Machine Learning and Deep Learning techniques.

This repository contains the Machine Learning module developed for the SIEM project using the CICIDS2017 dataset.

---

## Project Overview

Traditional SIEM systems rely on rule-based detection, which often produces a large number of false positives and struggles to identify unknown attacks.

This project applies anomaly detection techniques to improve network intrusion detection by using:

- Isolation Forest (Machine Learning)
- LSTM Autoencoder (Deep Learning)

The models are trained using the CICIDS2017 intrusion detection dataset and are designed to classify network traffic as either:

- Normal
- Attack

---

## Features

- Data preprocessing and cleaning
- Feature engineering
- Feature scaling using StandardScaler
- Isolation Forest anomaly detection
- LSTM Autoencoder anomaly detection
- Model evaluation
- Prediction module for deployment
- Ready for backend API integration

---

## Project Structure

```text
ml/
│
├── notebooks/
│   ├── attack_analysis.ipynb
│   ├── isolation_forest.ipynb
│   ├── lstm_autoencoder.ipynb
│   └── model_evaluation.ipynb
│
├── predict.py
├── requirements.txt
│
├── dataset/          (Google Drive)
├── models/           (Google Drive)
├── results/          (Generated after evaluation)
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow / Keras
- Matplotlib
- Joblib
- Jupyter Notebook

---

## Dataset

Dataset Used:

**CICIDS2017 Intrusion Detection Dataset**

The dataset is too large to upload to GitHub.

Download it from the shared Google Drive and place it inside:

```text
ml/dataset/
```

---

## Trained Models

The trained models are also stored separately because of their size.

Place the following files inside:

```text
ml/models/
```

Required files:

```text
scaler.pkl
isolation_forest.pkl
lstm_autoencoder.keras
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Mr-PratikPaudel/siem-ai-project.git
```

Move into the project directory:

```bash
cd siem-ai-project
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r ml/requirements.txt
```

---

## Workflow

```
CICIDS2017 Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Feature Scaling
        │
        ▼
Train/Test Split
        │
 ┌───────────────┐
 │               │
 ▼               ▼
Isolation     LSTM
Forest      Autoencoder
 │               │
 └──────┬────────┘
        ▼
 Model Evaluation
        ▼
 Prediction Module
```

---

## Model Evaluation

Both models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Running the Project

### Train Isolation Forest

Run:

```
notebooks/isolation_forest.ipynb
```

---

### Train LSTM Autoencoder

Run:

```
notebooks/lstm_autoencoder.ipynb
```

---

### Evaluate Models

Run:

```
notebooks/model_evaluation.ipynb
```

---

### Prediction

Run:

```bash
python ml/predict.py
```

---

## Current Project Status

Completed

- Data preprocessing
- Attack analysis
- Feature scaling
- Isolation Forest training
- LSTM Autoencoder training
- Model evaluation
- Prediction module

Upcoming

- Backend API (Flask/FastAPI)
- Frontend Dashboard
- Real-time Log Monitoring
- Elasticsearch Integration
- Kafka Integration
- SIEM Dashboard
- Threat Visualization

---

## Team Members

- Pratik Paudel
- Subekshya KC
- Helan Basnet
- Laxmi Saud

---

## Future Improvements

- Real-time network traffic monitoring
- Log aggregation
- Threat intelligence integration
- Explainable AI (XAI)
- Model optimization
- Ensemble anomaly detection
- Automated incident response

---

## License

This project is developed for educational and research purposes.

---

## Acknowledgements

- CICIDS2017 Dataset
- TensorFlow
- Scikit-learn
- Keras
- Pandas
- NumPy
