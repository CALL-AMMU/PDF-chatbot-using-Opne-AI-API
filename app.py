import streamlit as st
import openai
import os
from PyPDF2 import PdfReader
from datetime import datetime

# Set OpenAI API key (from environment variable)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_pdf_text(pdf_file):
    # Extract text from PDF using PyPDF2
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def chat_with_pdf(pdf_file, user_query):
    # Process PDF text
    pdf_text = get_pdf_text(pdf_file)

    # Fine-tune response based on specific requirements
    # (e.g., summarizing key points, answering specific questions)
    prompt = f"You have uploaded a PDF document. The user asks: {user_query}. Summarize the relevant information from the PDF and provide a concise response."
    response = openai.Completion.create(
        engine="text-davinci-003",  # Adjust engine as needed
        prompt=prompt,
        max_tokens=1024,  # Adjust token limit for longer responses
        n=1,
        stop=None,
        temperature=0.7,  # Adjust temperature for creativity vs. accuracy
        top_p=1,
    )

    return response.choices[0].text.strip()

st.title("Conversational PDF Chatbot with OpenAI")

uploaded_file = st.file_uploader("Upload a PDF file")

if uploaded_file is not None:
    chat_history = []  # Maintain conversation history (optional)

    while True:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")  # Unique timestamp
        user_query = st.text_input("Ask a question about the PDF:", key=f"user_query_{timestamp}")

        if user_query:
            response = chat_with_pdf(uploaded_file, user_query)
            chat_history.append((user_query, response))

            st.write("**You:**", user_query)
            st.write("**Chatbot:**", response)

            # Optionally, display conversation history
            if st.checkbox("Show Conversation History"):
                for query, resp in chat_history:
                    st.write(f"- You: {query}")
                    st.write(f"- Chatbot: {resp}")

        if st.button("End Chat", key=f"end_chat_{timestamp}"):
            break

else:
    st.write("Please upload a PDF file to begin.")
