import joblib
import re

# Load pre-trained model
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")  # Add if using TF-IDF etc.

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()

def predict_text(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    pred = model.predict(vector)[0]
    return "Cyberbullying" if pred == 1 else "Not Cyberbullying"
