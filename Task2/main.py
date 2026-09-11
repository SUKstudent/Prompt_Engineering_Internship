import os
from google import genai
from dotenv import load_dotenv

print("Project 2: CoT Logic Engine")
print("----------------------------")

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

question = input("\nEnter your logic question: ")

prompt = f"""
Solve the following logic problem carefully.

Problem:
{question}

Instructions:
1. Analyze the problem step by step.
2. Do not make assumptions that are not given.
3. After solving, perform a self-check to verify the logic.
4. If you find an error during the self-check, correct it.
5. Give the final answer clearly.

Format your response as:

Problem:
Reasoning Summary:
Self-check:
Final answer:
"""

print("\nSolving and self-checking...\n")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={
        "temperature": 0
    }
)

print(response.text)