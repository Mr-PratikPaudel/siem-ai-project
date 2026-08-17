import sys
sys.path.insert(0, "ml")

import pandas as pd
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# -----------------------------
# Paths
# -----------------------------
DATASET = "ml/dataset/clean_dataset_sample.csv"
MODELS = "ml/models"

# -----------------------------
# Load models
# -----------------------------
print("Loading models...")

scaler = joblib.load(f"{MODELS}/scaler.pkl")
iso_model = joblib.load(f"{MODELS}/isolation_forest.pkl")
lstm_model = load_model(f"{MODELS}/lstm_autoencoder.keras")

print("Models loaded.")

# -----------------------------
# Load a balanced sample
# -----------------------------
print("Loading dataset sample...")

df = pd.read_csv(
    DATASET,
    encoding="utf-16",
    nrows=20000
)

# 10,000 Normal + 10,000 Attack if available
normal = df[df["Label"] == 0]
attack = df[df["Label"] == 1]

n = min(len(normal), len(attack), 5000)

normal = normal.iloc[:n]
attack = attack.iloc[:n]

test_df = pd.concat([normal, attack], ignore_index=True)

X = test_df.drop("Label", axis=1)
y = test_df["Label"].values

print("Samples:", len(test_df))
print("Normal:", sum(y == 0))
print("Attack:", sum(y == 1))

# -----------------------------
# Scale
# -----------------------------
X_scaled = scaler.transform(X)

# -----------------------------
# Isolation Forest
# -----------------------------
print("\nRunning Isolation Forest...")

iso_predictions = iso_model.predict(X_scaled)

# Isolation Forest:
# -1 = anomaly/attack
#  1 = normal
iso_pred = np.where(iso_predictions == -1, 1, 0)

# -----------------------------
# LSTM Autoencoder
# -----------------------------
print("Running LSTM Autoencoder...")

X_lstm = np.expand_dims(X_scaled, axis=1)

reconstructed = lstm_model.predict(
    X_lstm,
    verbose=0
)

mse = np.mean(
    np.square(X_lstm - reconstructed),
    axis=(1, 2)
)

lstm_pred = np.where(mse > 0.02, 1, 0)

# -----------------------------
# Metrics function
# -----------------------------
def show_results(name, y_true, y_pred):

    tn, fp, fn, tp = confusion_matrix(
        y_true,
        y_pred,
        labels=[0, 1]
    ).ravel()

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    fpr = fp / (fp + tn) if (fp + tn) else 0

    print("\n==============================")
    print(name)
    print("==============================")

    print("TP:", tp)
    print("FP:", fp)
    print("TN:", tn)
    print("FN:", fn)

    print("Accuracy:", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall:", round(recall, 4))
    print("F1 Score:", round(f1, 4))
    print("False Positive Rate:", round(fpr, 4))


# -----------------------------
# Results
# -----------------------------
show_results(
    "Isolation Forest",
    y,
    iso_pred
)

show_results(
    "LSTM Autoencoder",
    y,
    lstm_pred
)