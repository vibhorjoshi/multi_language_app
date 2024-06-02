# translator.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

def translate(text, tokenizer, model, source_lang, target_lang):
    inputs = tokenizer(f"translate {source_lang} to {target_lang}: {text}", return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=100, num_beams=4, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

if __name__ == "__main__":
    model_name = "Helsinki-NLP/opus-mt-en-fr"  # Example model, change as needed
    tokenizer, model = load_model(model_name)
    text = "Hello, how are you?"
    translated_text = translate(text, tokenizer, model, "en", "fr")
    print(f"Translated text: {translated_text}")
