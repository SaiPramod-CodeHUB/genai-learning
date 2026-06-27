# 🤖 Generative AI + Agentic Learning Journey
**Author:** Sai Pramod Gopireddy  
**GitHub:** SaiPramod-CodeHUB  
**Course:** Complete GenAI + LangChain + LangGraph + RAG + Agents  
**Certification Target:** Anthropic Claude Certified Architect (CCA-F) — Sep 1, 2026  
**Started:** June 21, 2026  

---

## 🎯 Goal
Build GenAI expertise from LangChain basics → Production-ready AI agents → CCA-F Certified by Sep 1, 2026

---

## 📚 9-Week Course Structure

| Week | Dates | Topic | Status |
|------|-------|-------|--------|
| Week 1–2 | Jun 21 – Jul 8 | LangChain Basics | 🔄 In Progress |
| Week 3–4 | Jul 9 – Jul 22 | LangGraph + Agents | ⏳ Upcoming |
| Week 5–6 | Jul 23 – Aug 5 | RAG Systems + Vectorless RAG | ⏳ Upcoming |
| Week 7 | Aug 6 – Aug 12 | Deep Agents + Guardrails | ⏳ Upcoming |
| Week 8 | Aug 13 – Aug 19 | LLM Evaluation + Gateways | ⏳ Upcoming |
| Week 9 | Aug 20 – Sep 1 | CCA-F Exam Prep | ⏳ Upcoming |

---

## 📁 Project Structure

```
genai-learning/
├── week1-langchain/
│   ├── langchain_basics.py          # Project 1 — Prompt Templates + Groq LLM
│   └── resume_bullet_generator.py   # Project 2 — AI Resume Bullet Generator
├── .env.example                      # API key template (never commit .env)
├── .gitignore
└── README.md
```

---

## ✅ Week 1 — LangChain Basics (Jun 21 – Jul 8)

### Project 1 — LangChain Basics
- ✅ Installed LangChain + langchain-groq + python-dotenv
- ✅ Created ChatPromptTemplate with variables
- ✅ Connected Groq LLM (llama-3.3-70b-versatile)
- ✅ Built first chain: Prompt → LLM → Response
- ✅ Got real AI response
- ✅ Pushed to GitHub

### Project 2 — Resume Bullet Generator
- ✅ Built LangChain chain for resume writing
- ✅ Takes raw experience as input
- ✅ Generates metrics-driven resume bullets using AI
- ✅ Tested with real Apple work experience
- ✅ Pushed to GitHub

### What I learned this week
- LangChain is like Spring Boot for AI — structured, composable, reusable
- ChatPromptTemplate creates reusable prompts with {variable} placeholders
- The pipe operator (|) chains components: prompt | llm
- invoke() runs the full chain end to end
- API keys must ALWAYS go in .env file — never hardcoded
- Groq provides free LLM API (llama-3.3-70b-versatile)

---

## ⚙️ Setup

```bash
# Install dependencies
pip install langchain langchain-groq python-dotenv

# Setup API key
cp .env.example .env
# Add your Groq API key to .env

# Run projects
python week1-langchain/langchain_basics.py
python week1-langchain/resume_bullet_generator.py
```

Get free Groq API key: https://console.groq.com  
Anthropic Academy (free courses): https://anthropic.skilljar.com  
CCA-F Practice questions: https://certsafari.com/anthropic/claude-certified-architect

---

## 🏆 Certifications Target

| Cert | Provider | Target Date | Status |
|------|----------|-------------|--------|
| Claude Certified Architect (CCA-F) | Anthropic | Sep 1, 2026 | ⏳ Studying |

---

## 💼 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
