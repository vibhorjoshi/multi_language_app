# app.py
import streamlit as st
from translator import load_model, translate
from speech_recognition import recognize_speech

# Load translation models
model_name = "Helsinki-NLP/opus-mt-en-fr"  # Example model, change as needed
tokenizer, model = load_model(model_name)

st.title("Multi-Language Translator and Speech Recognizer")

# Translation section
st.header("Text Translation")
source_text = st.text_area("Enter text to translate")
source_lang = st.selectbox("Source Language", ["en", "fr", "de", "es"])  # Add languages as needed
target_lang = st.selectbox("Target Language", ["en", "fr", "de", "es"])  # Add languages as needed

if st.button("Translate"):
    translated_text = translate(source_text, tokenizer, model, source_lang, target_lang)
    st.write("Translated Text:")
    st.write(translated_text)

# Speech recognition section
st.header("Speech Recognition")
uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])

if uploaded_file is not None:
    recognized_text = recognize_speech(uploaded_file)
    st.write("Recognized Text:")
    st.write(recognized_text)
