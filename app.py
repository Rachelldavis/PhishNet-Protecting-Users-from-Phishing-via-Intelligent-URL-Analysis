import streamlit as st
import pandas as pd
import joblib

# Load model and feature names
model = joblib.load("url_model.pkl")
features = joblib.load("feature_names.pkl")

st.title("🔐 SafeSpeak: URL Phishing Detector")

# Collect inputs
url_length = st.number_input("URL Length", min_value=0)
is_domain_ip = st.selectbox("Is Domain an IP?", [0, 1])
url_similarity = st.slider("URL Similarity Index (0 to 100)", 0.0, 100.0)
letter_ratio = st.slider("Letter Ratio in URL", 0.0, 1.0)
digit_ratio = st.slider("Digit Ratio in URL", 0.0, 1.0)
num_equals = st.number_input("Number of '=' in URL", min_value=0)
num_qmark = st.number_input("Number of '?' in URL", min_value=0)
num_amp = st.number_input("Number of '&' in URL", min_value=0)
special_char_ratio = st.slider("Special Character Ratio in URL", 0.0, 1.0)
is_https = st.selectbox("Is HTTPS?", [0, 1])

# Put all inputs into a DataFrame in correct order
input_data = pd.DataFrame([[
    url_length,
    is_domain_ip,
    url_similarity,
    letter_ratio,
    digit_ratio,
    num_equals,
    num_qmark,
    num_amp,
    special_char_ratio,
    is_https
]], columns=features)

# Predict button
if st.button("Detect"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ This URL is likely a PHISHING site.")
    else:
        st.success("✅ This URL appears to be SAFE.")
