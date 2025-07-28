import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv('phishing_data.csv')

# Use actual feature columns from your dataset
features = [
    'URLLength',
    'IsDomainIP',
    'URLSimilarityIndex',
    'LetterRatioInURL',
    'DegitRatioInURL',
    'NoOfEqualsInURL',
    'NoOfQMarkInURL',
    'NoOfAmpersandInURL',
    'SpacialCharRatioInURL',
    'IsHTTPS'
]

# Define X and y
X = df[features]
y = df['label']  # 0 = legitimate, 1 = phishing

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and features
joblib.dump(model, 'url_model.pkl')
joblib.dump(features, 'feature_names.pkl')

print("✅ Model saved successfully!")
