import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("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")

if not api_key:
    st.error("Please provide a valid OpenAI API key in the .env file.")
else:
    openai.api_key = api_key

# App Title
st.title("ChatGPT Clone2")
st.write("Powered by OpenAI GPT")

# Input Area
user_input = st.text_area("Enter your message:")

if st.button("Submit"):
    if user_input.strip():
        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
            )
            # Display the AI's response
            st.success(response['choices'][0]['message']['content'].strip())
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before submitting.")
