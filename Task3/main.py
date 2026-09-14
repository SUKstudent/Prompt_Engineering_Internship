import os
from google import genai
from dotenv import load_dotenv

print("Project 3: Context-Anchored Answering (RAG Basics)")
print("------------------------------------------------")

# Load API key from .env
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Read reference document
with open("reference.txt", "r") as file:
    reference = file.read()

# Take user's question
question = input("\nAsk a question about Sony: ")

# Create RAG prompt
prompt = f"""
Answer the user's question using ONLY the reference context below.

REFERENCE CONTEXT:
{reference}

USER QUESTION:
{question}

Rules:
1. Use only the information provided in the reference context.
2. Do not use outside knowledge.
3. If the answer is not present in the reference, return exactly:
Information Not Found
4. If the answer is present, give the answer and mention the exact
sentence from the reference that supports it.
"""

print("\nGenerating answer...\n")

# Generate answer
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={
        "temperature": 0
    }
)

print("Answer:")
print(response.text)