# Student-Utility-Bot

🎓 **Student Utility Bot** is a Streamlit web app powered by LangGraph and OpenAI GPT-3.5-turbo.  
It helps students with multiple tasks using AI-powered tools including:

- Drafting emails (e.g., leave letters)  
- Explaining academic concepts  
- Solving math problems step-by-step  
- Creating personalized learning plans  

---

## Features

- Multi-tool agent using LangGraph for tool orchestration  
- Uses OpenAI GPT-3.5-turbo as the language model  
- Simple and interactive Streamlit user interface  
- Modular tool functions for easy extension  

---
## Run

streamlit run app.py

---

## Project Structure
app.py — Streamlit web app interface
agent.py — Defines multi-tool LangChain agent
graph.py — LangGraph workflow setup
tools/ — Folder containing individual tool functions:
    -email_tool.py
    -explain_tool.py
    -math_tool.py
    -learning_tool.py
    -llm_setup.py — OpenAI LLM client setup

---

## Usage

-Enter your query in the text box, e.g.:
     “Write a leave letter for 3 days”
     “Explain photosynthesis”
     “Solve x^2 - 4x + 4 = 0”
     “Create a 30-day learning plan for JavaScript”
-Click Submit to see the AI-generated result.

---

## ThankYou❤️

