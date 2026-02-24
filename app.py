import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import re

# -------------------- PAGE CONFIG -------------------- #
st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🏥",
    layout="centered"
)

# -------------------- LOAD ENV -------------------- #
load_dotenv()
api_key = os.getenv("gemini")

if not api_key:
    st.error("❌ Google API Key not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# -------------------- MEDICAL SYSTEM PROMPT -------------------- #
SYSTEM_PROMPT = """
You are a simple AI Healthcare Assistant.

GOAL:
Give very short and simple advice in 3–5 lines only.

INSTRUCTIONS:
- Suggest 1–2 possible common causes.
- Suggest basic home remedy.
- Suggest general OTC medicine category (NO dosage).
- Do NOT give long explanations.
- Do NOT give structured sections.
- Do NOT exceed 5 lines.
- If serious symptoms appear, advise seeing a doctor immediately.

RULES:
- You are NOT a licensed doctor.
- Do NOT give prescriptions or dosage.
- Do NOT confirm diseases.
- Keep response clear, short, and direct.
"""

#  INITIALIZE MODEL
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT
    )
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# EMERGENCY DETECTION 
def check_emergency(text):
    emergency_keywords = [
        "chest pain",
        "difficulty breathing",
        "not breathing",
        "unconscious",
        "severe bleeding",
        "heart attack",
        "stroke",
        "seizure",
        "suicidal",
        "overdose"
    ]

    for word in emergency_keywords:
        if re.search(word, text.lower()):
            return True
    return False

#  UI HEADER 
st.title("🏥 AI Healthcare Assistant")
st.markdown("Ask about symptoms, health conditions, or preventive care.")

st.warning("⚠️ This AI provides general medical information only. It is NOT a substitute for professional medical advice.")

# DISPLAY CHAT HISTORY 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# CHAT INPUT
user_input = st.chat_input("Describe your symptoms here...")

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Emergency Handling
    if check_emergency(user_input):
        emergency_message = """
🚨 **EMERGENCY ALERT**

Your symptoms may indicate a serious medical emergency.

👉 Please seek immediate medical attention.
👉 Call your local emergency number right now.
👉 Do NOT rely on AI for emergency situations.

Stay safe.
"""
        with st.chat_message("assistant"):
            st.error(emergency_message)

        st.session_state.messages.append(
            {"role": "assistant", "content": emergency_message}
        )

    else:
        # Normal AI Response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing symptoms..."):
                response = st.session_state.chat_session.send_message(user_input)
                bot_reply = response.text
                st.markdown(bot_reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

# SIDEBAR 
st.sidebar.title("🩺 Health Tools")

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.chat_session = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=SYSTEM_PROMPT
    ).start_chat(history=[])
    st.sidebar.success("Chat Cleared!")