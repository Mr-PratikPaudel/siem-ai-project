import sys
sys.path.insert(0, "ml")

import pandas as pd
from predict import predict

DATASET = "ml/dataset/clean_dataset_sample.csv"

normal = None
attack = None
features = None

print("Searching dataset...")

for df in pd.read_csv(DATASET, encoding="utf-16", chunksize=10000):

    if features is None:
        features = [c for c in df.columns if c != "Label"]

    if normal is None:
        normal_rows = df[df["Label"] == 0]

        if len(normal_rows) > 0:
            normal = normal_rows[features].iloc[[0]]

    if attack is None:
        attack_rows = df[df["Label"] == 1]

        if len(attack_rows) > 0:
            attack = attack_rows[features].iloc[[0]]

    if normal is not None and attack is not None:
        break

print("\nNORMAL ROW:")
print(predict(normal))

print("\nATTACK ROW:")
print(predict(attack))