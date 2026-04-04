import PyPDF2
from openai import OpenAI
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()

# the text extractor:
def extract_text_from_pdf(pdf_path):
    text = ""

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # looping through every page and grabbing the text:
        for page in reader.pages:
            text += page.extract_text()
        
    return text[:15000]

# the ai brain:
def ask_ai_about_pdf(pdf_text, user_question):
    max_tokens=300
    client = OpenAI(api_key=os.getenv('OPEN_AI_API_KEY'))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Use the following document text to answer the user's question. If the answer isn't in the text, say you don't know."},
            {"role": "user", "content": f"Document Text: {pdf_text}"},
            {"role": "user", "content": f"Question: {user_question}"}
        ]
    )
    return response.choices[0].message.content