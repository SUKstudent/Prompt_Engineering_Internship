# Decode Labs
## Prompt Engineering
# Decode Labs
## Prompt Engineering
## Task 1 - Zero-Shot & Few-Shot Data Extraction using Gemini

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

## Rules:
1. Return JSON only.
2. Do not use markdown code blocks.
3. Do not add any explanation or conversational text.
4. If any field is missing, use null.
5. Keep the exact information found in the input.
6. The output must be valid JSON.
Few-Shot Examples

### Example 1

### Input:

Aman Verma is 28 years old and works at TCS.
He lives in Mumbai and his email is aman@gmail.com.

### Output:

{
    
    "name": "Aman Verma",
    
    "age": 28,
    
    "company": "TCS",
    
    "city": "Mumbai",
    
    "email": "aman@gmail.com"
}

### Example 2

### Input:

Priya Singh is 32 years old and works at Wipro.
She lives in Delhi and her email is priya@gmail.com.

### Output:

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

# Project 2: CoT Logic Engine

## Overview

This project is a Chain-of-Thought (CoT) Logic Engine that uses the Gemini API to solve multi-step logic problems.

The system accepts a logic question from the user, analyzes the problem step by step, performs a self-check of the solution, and provides the final answer.

## Objective

The main objective of this project is to guide an AI model to:

* Solve complex logic problems systematically
* Avoid incorrect assumptions
* Review its own reasoning
* Correct errors when found
* Provide a clear final answer

## How It Works

The workflow is:

**User Input → Logic Analysis → Self-Check → Final Answer**

1. The user enters a logic question.
2. The question is sent to the Gemini API with a structured prompt.
3. Gemini analyzes the problem step by step.
4. The model performs a self-check to verify the solution.
5. The final answer is displayed to the user.

## Technologies Used

* Python
* Google Gemini API
* Google GenAI SDK
* python-dotenv

## Prompting Technique

This project uses Chain-of-Thought (CoT) prompting to encourage systematic reasoning.

The prompt also includes a **Self-Check** phase where the model reviews its solution before giving the final answer.

## Testing

### Test 1: Sheep Logic Trap

**Question:**

> A farmer has 17 sheep. All but 9 run away. How many sheep are left?

**Final Answer:** 9 sheep

### Test 2: Bat and Ball Logic Trap

**Question:**

> A bat and a ball cost $1.10 in total. The bat costs $1 more than the ball. How much does the ball cost?

**Final Answer:** $0.05 (5 cents)

Both tests were successfully solved with a reasoning summary and self-check.

## Project Structure

```text
Project-2-CoT-Logic-Engine/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

> Note: `.env` contains the API key and should not be uploaded to GitHub.

## How to Run

### 1. Install dependencies

python -m pip install -U google-genai python-dotenv


### 2. Add the Gemini API key

Create a `.env` file:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY


### 3. Run the project

python main.py`

### 4. Enter a logic question

The program will analyze the question, perform a self-check, and display the final answer.

## Conclusion

This project demonstrates the use of Chain-of-Thought prompting, algorithmic reasoning, self-correction, and structured problem solving for logic-based questions.
