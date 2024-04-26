# PDF-chatbot-using-Opne-AI-API

1. Project Setup and Dependencies:

Create a virtual environment (recommended):

Bash
python3 -m venv openai_chatbot_env
source openai_chatbot_env/bin/activate

Install required libraries:

Bash
pip install openai streamlit PyPDF2

Obtain your OpenAI API key:
Create a free account at https://openai.com/
Go to your API keys and generate a new one. Store it securely (we'll use an environment variable for security).

Bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

2. Streamlit App Development:

Create a Python file (e.g., app.py):

Python

import streamlit as st
import openai
from PyPDF2 import PdfReader

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
        user_query = st.text_input("Ask a question about the PDF:")

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

        if st.button("End Chat"):
            break

else:
    st.write("Please upload a PDF file to begin.")

Use code with caution.
content_copy
3. Streamlit App Deployment:

Run the app locally:

Bash
streamlit run app.py


This opens your default browser at http://localhost:8501 to access the chatbot.

For production deployment (optional):

Explore cloud platforms like Heroku or Google Cloud Run that offer free tiers.
These platforms provide instructions for deploying Streamlit apps.
Key Improvements and Considerations:

Clarity and Maintainability: The code is well-structured with comments and clear function definitions.
PDF Text Extraction: Uses PyPDF2 for robust text extraction from PDFs.
OpenAI API Key Security: Employs an environment variable for secure storage of the API key.
Prompt Fine-Tuning: Provides a general prompt template but emphasizes the importance of customizing it based on your specific requirements (e.g., summarizing key points, answering specific types of questions). Experiment with different engine types, temperature, and other parameters to fine-tune the response style and accuracy.
Conversation History (Optional): Allows you to
