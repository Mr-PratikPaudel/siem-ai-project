import pandas as pd


# ==========================================================
# 1. LOAD DATASET
# ==========================================================

dataset_path = "ml/dataset/clean_dataset_sample.csv"

df = pd.read_csv(dataset_path)

print("Dataset loaded successfully!")
print("Total samples:", len(df))


# ==========================================================
# 2. DEFINE RULE
# ==========================================================

# Simple rule:
# If SYN Flag Count > 1 → Attack
# Otherwise → Normal

df["Rule_Prediction"] = (
    df["SYN Flag Count"] > 1
).astype(int)


# ==========================================================
# 3. COMPARE RULE WITH ACTUAL LABEL
# ==========================================================

actual = df["Label"]
predicted = df["Rule_Prediction"]


# True Positive
true_positive = (
    (actual == 1) &
    (predicted == 1)
).sum()


# False Positive
false_positive = (
    (actual == 0) &
    (predicted == 1)
).sum()


# True Negative
true_negative = (
    (actual == 0) &
    (predicted == 0)
).sum()


# False Negative
false_negative = (
    (actual == 1) &
    (predicted == 0)
).sum()


# ==========================================================
# 4. CALCULATE FALSE POSITIVE RATE
# ==========================================================

normal_samples = (actual == 0).sum()

false_positive_rate = (
    false_positive / normal_samples
) * 100


# ==========================================================
# 5. DISPLAY RESULTS
# ==========================================================

print("\n================================")
print("RULE-BASED BASELINE RESULTS")
print("================================")

print("Total samples:", len(df))

print("True Positives:", true_positive)

print("False Positives:", false_positive)

print("True Negatives:", true_negative)

print("False Negatives:", false_negative)

print(
    "False Positive Rate:",
    round(false_positive_rate, 2),
    "%"
)