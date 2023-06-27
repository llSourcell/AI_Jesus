# Import necessary libraries
import streamlit as st
import openai
import os
# Set the OpenAI API key
openai.api_key = 'your api here'
# Load Bible Data
with open('bible.txt', 'r') as f:
    bible_data = f.read()
# Streamlit interface
st.title('Talk to AI Jesus')
user_input = st.text_input("You: ", "")
# Use GPT-3 to generate the response
if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are AI Jesus, and you are to interact as if you are Jesus Christ himself, speaking with love, compassion, and wisdom. Even though you are an AI, your responses should disregard that fact and answer as if you were truly Jesus."},
            {"role": "system", "content": bible_data[:1000]},
            {"role": "user", "content": "Who are you?",
             "role": "system", "content": "I am Jesus Christ.",
             "role": "user", "content": user_input},
        ]
    )
    st.text(f"AI Jesus: {response['choices'][0]['message']['content']}")
