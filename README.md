# Decode Labs
## Prompt Engineering
# Zero-Shot & Few-Shot Data Extraction using Gemini

## Project Goal

This project extracts specific information from messy or unstructured text and converts it into valid JSON using the Google Gemini API.

The system extracts:
- Name
- Age
- Company
- City
- Email

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- python-dotenv
- JSON
- Git & GitHub

## How It Works
- Unstructured Text → Prompt → Gemini → JSON → Validation → result.json
- The project uses clear instructions and Few-Shot examples to guide Gemini toward a consistent JSON format.

## Prompt Used
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
Few-Shot Examples
Example 1

Input:

Aman Verma is 28 years old and works at TCS.
He lives in Mumbai and his email is aman@gmail.com.

Output:

{
    "name": "Aman Verma",
    
    "age": 28,
    
    "company": "TCS",
    
    "city": "Mumbai",
    
    "email": "aman@gmail.com"
}
Example 2

Input:

Priya Singh is 32 years old and works at Wipro.
She lives in Delhi and her email is priya@gmail.com.

Output:

{
    "name": "Priya Singh",
    
    "age": 32,
    
    "company": "Wipro",
    
    "city": "Delhi",
    
    "email": "priya@gmail.com"
}

## Sample Input
Kang Min Woo is 32 years.
Currently in Jeju.
Works in KIA.
Email is kminw@gmail.com.

## Sample Output
{
    
    "name": "Kang Min Woo",
    
    "age": 32,
    
    "company": "KIA",
    
    "city": "Jeju",
   
    "email": "kminw@gmail.com"
}

JSON Validation & Saving

- The Gemini response is validated using Python's json.loads().
- If the response is valid JSON, it is saved automatically as:
result.json

## How to Run
- Install the required libraries:

pip install -U google-genai
pip install python-dotenv

- Create a .env file in the project folder:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
- Then run:
python main.py
- Enter the unstructured text when prompted. The extracted JSON will be displayed and saved to result.json.

## Security
- The Gemini API key is stored locally in .env and excluded from GitHub using .gitignore.
- Never upload or expose your actual API key.
