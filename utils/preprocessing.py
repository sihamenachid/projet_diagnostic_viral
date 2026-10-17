import csv


def load_patient_data(path):
    """Charge le CSV et le sépare en X (données patient) et y (étiquettes)."""
    X, y = [], []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            y.append(int(row.pop("infecte")))
            X.append({
                "temperature": float(row["temperature"]),
                "fievre": int(row["fievre"]),
                "toux": int(row["toux"]),
                "fatigue": int(row["fatigue"]),
            })
    return X, y


def train_test_split(X, y, test_ratio=0.2, seed=42):
    """Mélange les données puis les sépare : 80 % entraînement, 20 % test."""
    import random
    indices = list(range(len(X)))
    random.Random(seed).shuffle(indices)
    n_test = int(len(X) * test_ratio)
    test_idx, train_idx = indices[:n_test], indices[n_test:]
    X_train = [X[i] for i in train_idx]
    y_train = [y[i] for i in train_idx]
    X_test = [X[i] for i in test_idx]
    y_test = [y[i] for i in test_idx]
    return X_train, X_test, y_train, y_test
