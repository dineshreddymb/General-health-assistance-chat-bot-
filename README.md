# 🏥 AI Healthcare Assistant

An AI-powered Healthcare Assistant built using **Google Gemini API** and **Streamlit**, designed to provide short, simple, and responsible medical guidance with built-in safety guardrails and emergency detection.

> ⚠️ This application provides general medical information only. It is NOT a substitute for professional medical advice.

---

## 🚀 Live Demo

🌐 http://13.62.222.190:8501

---

## 📌 Project Overview

The AI Healthcare Assistant is designed to:

- Provide short and clear responses (3–5 lines only)
- Suggest 1–2 possible common causes of symptoms
- Recommend basic home remedies
- Suggest general OTC medicine categories (NO dosage)
- Detect emergency symptoms and alert users immediately
- Avoid diagnosis confirmation or prescription

This project focuses on **Responsible AI Implementation** in sensitive domains like healthcare.

---

## 🔍 Problem Statement

Online medical searches often:

- Provide overwhelming or complex information
- Cause unnecessary panic
- Encourage unsafe self-diagnosis
- Lack emergency detection mechanisms

---

## 💡 Solution

This application introduces:

✅ Controlled Prompt Engineering  
✅ Strict Medical Guardrails  
✅ Emergency Keyword Detection System  
✅ Multi-turn Conversation Memory  
✅ Clean & Interactive Chat UI  
✅ Cloud Deployment on AWS EC2  

---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API (gemini-2.5-flash)**
- **AWS EC2**
- **dotenv (Environment Variable Management)**
- **Regex (Emergency Detection)**

---

## 🏗️ System Architecture

User → Streamlit UI → Gemini Model (with System Prompt) → Response  
Emergency Detection Layer → Immediate Alert (if required)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-healthcare-assistant.git
cd ai-healthcare-assistant
