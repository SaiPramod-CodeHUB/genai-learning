# ============================================================
# LangChain Basics - Day 1
# Author: Sai Pramod Gopireddy
# Date: June 24, 2026
# Course: Krish Naik - Generative AI + Agentic (LangChain/LangGraph)
# GitHub: SaiPramod-CodeHUB
# ============================================================

# ---- STEP 1: Install dependencies ----
# Run this in terminal or Colab:
# pip install langchain langchain-groq python-dotenv

# ---- STEP 2: Imports ----
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# ---- STEP 3: Load API key from .env file (NEVER hardcode keys) ----
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---- STEP 4: Initialize the LLM ----
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

# ---- STEP 5: Create a Prompt Template ----
prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Answer this: {question}"
)

# ---- STEP 6: Build the Chain (Prompt → LLM) ----
chain = prompt | llm

# ---- STEP 7: Invoke the Chain ----
response = chain.invoke({"question": "What is LangChain?"})
print("=" * 60)
print("RESPONSE:")
print("=" * 60)
print(response.content)

# ---- STEP 8: Try multiple questions ----
questions = [
    "What is a LangChain chain?",
    "What is a prompt template in LangChain?",
    "How is LangChain useful for Java developers?"
]

print("\n" + "=" * 60)
print("MULTIPLE QUESTIONS:")
print("=" * 60)
for q in questions:
    print(f"\nQ: {q}")
    res = chain.invoke({"question": q})
    print(f"A: {res.content[:300]}...")  # Print first 300 chars
    print("-" * 40)
