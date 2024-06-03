# app.py
import streamlit as st
from translator import load_model, translate
from speech_recog import recognize_speech,extract_audio_from_video
import os

# Load translation models
model_name = "Helsinki-NLP/opus-mt-en-fr" # Example model, change as needed
tokenizer, model = load_model(model_name)

st.title("Multi-Language Translator and Speech Recognizer")

# Ensure the 'audio' directory exists
if not os.path.exists("audio"):
    os.makedirs("audio")


uploaded_file = st.file_uploader("Upload an audio or video file", type=["wav", "mp4"])

if uploaded_file:
    file_path = os.path.join("audio", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    recognized_text = recognize_speech(file_path)
    st.write(f"Recognized Text: {recognized_text}")
    
# Translation section

st.header("Text Translation")
source_text = st.text_area("Enter text to translate")
source_lang = st.selectbox("Source Language", ["en", "fr", "de", "es"])  # Add languages as needed
target_lang = st.selectbox("Target Language", ["en", "fr", "de", "es"])  # Add languages as needed

if st.button("Translate"):
    translated_text = translate(source_text, tokenizer, model, source_lang, target_lang)
    st.write("Translated Text:")
    st.write(translated_text)

st.write("Translation model used: Helsinki-NLP/opus-mt-multi")


