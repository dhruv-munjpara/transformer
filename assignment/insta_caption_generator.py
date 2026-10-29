"""
SESSION 5: Streamlit Instagram Caption Generator
Tasks 1-5: Complete Streamlit app with Text Input, API Integration (Hugging Face / OpenAI via requests),
and a Chat Interface showing the last 3 user queries and AI-generated captions in chat bubbles.
"""

import streamlit as st
import requests
import os

# --- Task 1: Welcome Header ---
st.set_page_config(page_title="Insta Caption Generator", page_icon="📸", layout="centered")
st.title("Welcome to Insta Caption Generator! 📸✨")
st.markdown("Generate engaging, viral Instagram captions with hashtags using AI.")

# Initialize session state for storing chat history (Task 5: Last 3 interactions)
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar for API configuration
with st.sidebar:
    st.header("⚙️ Settings")
    api_choice = st.radio("Choose API Provider:", ["Hugging Face Free Inference API", "OpenAI API", "Demo / Local Fallback"])
    api_key = st.text_input("Enter API Key (Optional for Demo):", type="password")
    tone = st.selectbox("Caption Tone:", ["Trendy & Aesthetic", "Funny & Relatable", "Inspirational", "Minimalist"])

# --- Task 2: Input Box & Button ---
with st.form("caption_form", clear_on_submit=True):
    user_description = st.text_input("Describe your photo", placeholder="e.g., A golden hour selfie drinking iced coffee at a rooftop cafe")
    generate_btn = st.form_submit_button("Generate Caption")

# Helper function to call Hugging Face / OpenAI via requests (Task 4)
def fetch_ai_caption(description, tone, api_choice, api_key):
    prompt = f"Write a creative, catchy Instagram caption with matching emojis and hashtags for a photo described as: '{description}'. Tone: {tone}."

    if api_choice == "OpenAI API" and api_key:
        try:
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a professional social media manager crafting viral Instagram captions."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 120,
                "temperature": 0.8
            }
            res = requests.post(url, headers=headers, json=payload, timeout=15)
            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"].strip()
            else:
                st.warning(f"OpenAI API returned status {res.status_code}. Using local smart generator fallback.")
        except Exception as e:
            st.error(f"Error calling OpenAI API: {e}")

    elif api_choice == "Hugging Face Free Inference API":
        try:
            # Hugging Face Inference API for text generation (e.g., mistralai/Mistral-7B-Instruct-v0.3 or gpt2)
            url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
            headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
            payload = {"inputs": prompt, "parameters": {"max_new_tokens": 80, "temperature": 0.7}}
            res = requests.post(url, headers=headers, json=payload, timeout=15)
            if res.status_code == 200:
                result = res.json()
                if isinstance(result, list) and len(result) > 0:
                    text = result[0].get("generated_text", "")
                    # strip prompt if echoed
                    return text.replace(prompt, "").strip() or text
            else:
                st.info("HF Inference API busy or loading. Using local creative caption generator.")
        except Exception as e:
            st.warning(f"HF API request notice: {e}")

    # High quality fallback caption generator
    tone_emojis = {
        "Trendy & Aesthetic": "✨🌅🕊️",
        "Funny & Relatable": "☕😂🍕",
        "Inspirational": "🌟🚀💫",
        "Minimalist": "☁️🤍"
    }
    emoji = tone_emojis.get(tone, "✨")
    return f"{emoji} Chasing golden moments and making memories that never fade. {description}! #Vibes #{tone.replace(' ', '')} #InstaGood #GoldenHour #NoFilter"


# --- Task 3, 4 & 5: Processing Input, Displaying Description, and Chat Bubbles ---
if generate_btn and user_description.strip():
    with st.spinner("Brewing your Instagram caption..."):
        ai_caption = fetch_ai_caption(user_description, tone, api_choice, api_key)
        
        # Store in session state history
        st.session_state.history.append({
            "description": user_description,
            "caption": ai_caption
        })

# Display current/latest caption if available
if st.session_state.history:
    latest = st.session_state.history[-1]
    st.divider()
    # Task 3: Display user's input with 'Your Description:' label
    st.subheader("Your Description:")
    st.info(f"📌 {latest['description']}")
    
    # Task 4: Display AI Caption
    st.subheader("Generated AI Caption:")
    st.success(latest["caption"])

# --- Task 5: Chat Interface showing last 3 interactions in chat bubbles ---
st.divider()
st.subheader("💬 Recent Caption History (Last 3)")

# Keep only the last 3 items
last_3 = st.session_state.history[-3:]

if not last_3:
    st.caption("No captions generated yet. Enter a description above to get started!")
else:
    for idx, chat in enumerate(reversed(last_3), 1):
        # User bubble
        with st.chat_message("user"):
            st.write(f"**Photo Description:** {chat['description']}")
        # AI bubble
        with st.chat_message("assistant"):
            st.write(f"**Caption:** {chat['caption']}")

