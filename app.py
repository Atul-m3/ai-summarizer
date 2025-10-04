import streamlit as st # used to build web interface
from openai import OpenAI # needed to connect to GPT-3.5-Turbo model

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])# Load OpenAI client securely

st.set_page_config(page_title="AI Summarizer", layout="centered")# Set up Streamlit page
st.title("AI Summarizer & Q&A")# This shows the title on the web page top

def summarize_text(paragraph):# - Defines a function called summarize_text that takes a paragraph and returns a summary
    response = client.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the text clearly."},
            {"role": "user", "content": f"Summarize this:\n{paragraph}"}
        ]
    )
    return response.choices[0].message.content.strip() # Returns the summary from the model’s response, removing any extra spaces.

def answer_question(paragraph, question): # Function to answer question based on paragraph
    response = client.chat.completions.create( # This keeps the model focused on the given context.
        model="gpt-3.5-turbo", #uses gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "Answer questions only using the given paragraph."},
            {"role": "user", "content": f"Paragraph:\n{paragraph}\n\nQuestion:\n{question}"}
        ]
    )
    return response.choices[0].message.content.strip()# Returns the answer from the model’s response, cleaned up.

paragraph = st.text_area("Paste your paragraph here:", height=200) # Input: Paragraph, The height is set to 200 pixels for better readability.

if st.button("Summarize"): # Adds a button labeled “Summarize”. When clicked, it triggers the summarization.
    if paragraph.strip(): #removes leading and trailing spaces to return a copy of the original string
        st.subheader("Summary") # Displays a subheading titled ‘Summary’”
        st.write(summarize_text(paragraph)) # shows summarized code
    else:
        st.warning("Please enter a paragraph before summarizing.") # In case you enter null value, it will give this error

question = st.text_input("Ask a question about the paragraph:")# Input: Question

if question and paragraph:# Q&A Response
    st.subheader("Answer")
    st.write(answer_question(paragraph, question))
elif question and not paragraph:
    st.warning("Please enter a paragraph before asking a question.")# In case you enter null value, it will give this error
