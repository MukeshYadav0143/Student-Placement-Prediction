import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
import joblib
import os

def train():
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "processed_placement.csv")
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return

    print("Loading processed dataset...")
    df = pd.read_csv(data_path)

    X = df.drop(columns=["Placement_Status"])
    y = df["Placement_Status"]

    print(f"Dataset shape: {df.shape} | Features: {X.shape[1]}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=12,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_prob)

    print("\n==============================")
    print("      MODEL EVALUATION")
    print("==============================")
    print(f"Accuracy : {acc * 100:.2f}%")
    print(f"ROC-AUC  : {roc:.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Feature Importance
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
    print("\nTop 5 Important Features:")
    for feat, val in importances.head(5).items():
        print(f"  - {feat}: {val * 100:.2f}%")

    model_path = os.path.join(os.path.dirname(__file__), "..", "random_forest_placement_model.pkl")
    joblib.dump(model, model_path)
    print(f"\nModel saved successfully to: {model_path}")

if __name__ == "__main__":
    train()
