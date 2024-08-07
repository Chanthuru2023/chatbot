import streamlit as st
import requests

st.title("GPT-2 Chatbot")

user_input = st.text_input("Enter your message:")
if st.button("Generate Response"):
    response = requests.post(
        "http://localhost:5000/generate",
        json={"input_text": user_input}
    )
    response_data = response.json()
    st.write("Response:", response_data["response"])
