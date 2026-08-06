import joblib
import numpy as np
from tensorflow.keras.models import load_model

# -----------------------------
# Load Models
# -----------------------------
scaler = joblib.load("models/scaler.pkl")
iso_model = joblib.load("models/isolation_forest.pkl")
lstm_model = load_model("models/lstm_autoencoder.keras")

print("All Models Loaded Successfully!")


def predict_isolation_forest(sample):

    sample_scaled = scaler.transform(sample)

    prediction = iso_model.predict(sample_scaled)

    if prediction[0] == -1:
        return "Attack"

    return "Normal"

def predict_lstm(sample, threshold=0.02):

    sample_scaled = scaler.transform(sample)

    sample_lstm = np.expand_dims(sample_scaled, axis=1)

    reconstructed = lstm_model.predict(sample_lstm, verbose=0)

    mse = np.mean(
        np.square(sample_lstm - reconstructed),
        axis=(1, 2)
    )

    if mse[0] > threshold:
        return "Attack"

    return "Normal"

def predict(sample):

    iso_result = predict_isolation_forest(sample)

    lstm_result = predict_lstm(sample)

    return {
        "Isolation Forest": iso_result,
        "LSTM Autoencoder": lstm_result
    }

import pandas as pd

df = pd.read_csv("dataset/clean_dataset_sample.csv")

X = df.drop("Label", axis=1)

sample = X.iloc[[0]]

result = predict(sample)

print(result)

if __name__ == "__main__":

    import pandas as pd

    df = pd.read_csv("dataset/clean_dataset_sample.csv")

    X = df.drop("Label", axis=1)

    sample = X.iloc[[0]]

    result = predict(sample)

    print(result)