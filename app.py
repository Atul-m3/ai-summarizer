import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

st.set_page_config(page_title="AI Summarizer", layout="centered")
st.title("AI Summarizer & Q&A")

paragraph = st.text_area("Paste your paragraph here:", height=200)

if st.button("Summarize"):
    if paragraph.strip():
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the text clearly."},
                {"role": "user", "content": f"Summarize this:\n{paragraph}"}
            ]
        )
        st.subheader("Summary")
        st.write(response.choices[0].message.content.strip())

question = st.text_input("Ask a question about the paragraph:")

if question and paragraph:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Answer questions only using the given paragraph."},
            {"role": "user", "content": f"Paragraph:\n{paragraph}\n\nQuestion:\n{question}"}
        ]
    )
    st.subheader("Answer")
    st.write(response.choices[0].message.content.strip())