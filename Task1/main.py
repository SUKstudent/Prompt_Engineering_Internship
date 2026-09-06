import os
import json
from google import genai
from dotenv import load_dotenv

print("Prompt Engineering Project 1")
print("--------------------------------")

# Load API key from .env
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Take manual multi-line input
print("Enter your text below.")
print("When finished, press Ctrl+Z and then Enter (Windows).")
print()

lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

text = "\n".join(lines)

# Prompt with Few-Shot Examples
prompt = f"""
Extract the following information from the text:

- name
- age
- company
- city
- email

Rules:
1. Return JSON only.
2. Do not use markdown code blocks.
3. Do not add any explanation or conversational text.
4. If any field is missing, use null.
5. Keep the exact information found in the input.
6. The output must be valid JSON.

Here are some examples:

Example 1 - Input:
Aman Verma is 28 years old and works at TCS.
He lives in Mumbai and his email is aman@gmail.com.

Example 1 - Output:
{{
    "name": "Aman Verma",
    "age": 28,
    "company": "TCS",
    "city": "Mumbai",
    "email": "aman@gmail.com"
}}

Example 2 - Input:
Priya Singh is 32 years old and works at Wipro.
She lives in Delhi and her email is priya@gmail.com.

Example 2 - Output:
{{
    "name": "Priya Singh",
    "age": 32,
    "company": "Wipro",
    "city": "Delhi",
    "email": "priya@gmail.com"
}}

Now extract information from this user input:

Text:
{text}
"""

print("\nSending data to Gemini...\n")

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "temperature": 0
    }
)

# Display Gemini response
print("JSON Output:")
print(response.text)

# Validate and save JSON
try:
    data = json.loads(response.text)

    with open("result.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nValid JSON saved successfully!")
    print("File created: result.json")

except json.JSONDecodeError:
    print("\nInvalid JSON received from Gemini.")