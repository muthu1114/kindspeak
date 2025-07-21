import streamlit as st
import pandas as pd
import plotly.express as px
from model.predictor import predict_text

def load_sample_data():
    return pd.DataFrame({
        "Text": [
            "You're so dumb",
            "Have a nice day!",
            "No one likes you",
            "You're awesome!"
        ],
        "Prediction": [
            "Cyberbullying",
            "Not Cyberbullying",
            "Cyberbullying",
            "Not Cyberbullying"
        ]
    })

def main():
    st.set_page_config(page_title="Cyberbullying Detector", layout="wide")
    st.title("🛡️ Cyberbullying Detection Dashboard")

    # Input box
    st.subheader("💬 Test a Comment")
    user_input = st.text_area("Enter a social media comment:")
    
    if st.button("Predict"):
        if user_input.strip():
            prediction = predict_text(user_input)
            st.success(f"🧠 Prediction: **{prediction}**")
        else:
            st.warning("Please enter a comment to predict.")

    # Upload file and show stats
    st.markdown("---")
    st.subheader("📁 Bulk Upload (CSV)")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        if "Prediction" in df.columns:
            stats = df["Prediction"].value_counts().reset_index()
            stats.columns = ["Label", "Count"]
            fig = px.pie(stats, names="Label", values="Count", title="Cyberbullying vs Not Cyberbullying")
            st.plotly_chart(fig)
    else:
        st.info("No CSV uploaded. Showing sample data.")
        df = load_sample_data()
        st.dataframe(df)
