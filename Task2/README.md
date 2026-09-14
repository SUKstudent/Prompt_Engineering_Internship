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
