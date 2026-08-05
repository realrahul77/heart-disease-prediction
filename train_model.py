import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("heart.csv")

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)

# -----------------------------
# Binary Target
# -----------------------------
df["target"] = (df["num"] > 0).astype(int)

# -----------------------------
# Features
# -----------------------------
features = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalch",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]

X = df[features]
y = df["target"]

# -----------------------------
# Column Types
# -----------------------------
numeric_features = ["age", "trestbps", "chol", "thalch", "oldpeak", "ca"]

categorical_features = ["sex", "cp", "fbs", "restecg", "exang", "slope", "thal"]

# -----------------------------
# Preprocessing
# -----------------------------
numeric_transformer = Pipeline([("imputer", SimpleImputer(strategy="median"))])

categorical_transformer = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

# -----------------------------
# Pipeline
# -----------------------------
pipeline = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=200, random_state=42)),
    ]
)

# -----------------------------
# Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# -----------------------------
# Train
# -----------------------------
pipeline.fit(X_train, y_train)

# -----------------------------
# Evaluate
# -----------------------------
pred = pipeline.predict(X_test)

print("\nAccuracy :", round(accuracy_score(y_test, pred) * 100, 2), "%")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, pred))

print("\nClassification Report")
print(classification_report(y_test, pred))

# -----------------------------
# Save Pipeline
# -----------------------------
with open("model.pkl", "wb") as file:
    pickle.dump(pipeline, file)

print("\nPipeline saved successfully.")
