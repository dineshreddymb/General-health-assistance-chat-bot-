# 🏥 AI Healthcare Assistant
# 🏥 General Health Assistance Chat Bot

An AI-powered Healthcare Assistant built using **Google Gemini API** and **Streamlit**, designed to provide short, simple, and responsible medical guidance with built-in safety guardrails and emergency detection.

> ⚠️ This AI provides general medical information only. It is NOT a substitute for professional medical advice.

---

## 🚀 Live Demo

🌐 http://13.62.222.190:8501

---

## 📌 Project Overview

The **General Health Assistance Chat Bot** is designed to:

- Provide short and clear responses (3–5 lines only)
- Suggest 1–2 possible common causes of symptoms
- Recommend basic home remedies
- Suggest general OTC medicine categories (NO dosage)
- Detect emergency symptoms and alert users immediately
- Avoid diagnosis confirmation or prescription

This project focuses on implementing **Responsible AI in Healthcare**.

---

## 🔍 Problem Statement

Online medical searches often:

- Provide overwhelming and complex explanations
- Cause unnecessary anxiety
- Encourage unsafe self-diagnosis
- Lack emergency awareness mechanisms

---

## 💡 Solution

This AI system introduces:

✅ Controlled Prompt Engineering  
✅ Strict Medical Guardrails  
✅ Emergency Keyword Detection (Regex-based)  
✅ Multi-turn Conversation Memory  
✅ Clean Streamlit Chat Interface  
✅ AWS EC2 Cloud Deployment  

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- Google Gemini API (gemini-2.5-flash)  
- AWS EC2  
- dotenv (Environment Variable Management)  
- Regular Expressions (Emergency Detection)  

---

## 🏗️ System Architecture

User → Streamlit UI → Gemini Model (System Prompt Controlled) → AI Response  
                ↓  
        Emergency Detection Layer  
                ↓  
      🚨 Emergency Alert (If Triggered)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/General-health-assistance-chat-bot.git
cd General-health-assistance-chat-bot
