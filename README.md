
# Multi-Language Translator and Speech Recognizer

This project is a multi-language translator and speech recognizer application built with Streamlit. The application allows users to upload audio or video files, transcribe the speech to text, and translate the transcribed text into multiple languages.

## Features

- **Speech to Text**: Transcribes audio from `.wav` and `.mp4` files.
- **Multi-Language Translation**: Translates text between multiple languages.
- **User-Friendly Interface**: Built with Streamlit for a simple and interactive user experience.

## Models Used

- **Speech to Text**: The Google Web Speech API is used for converting speech to text. It is known for its accuracy and extensive language support.
- **Translation**: The `Helsinki-NLP/opus-mt-multi` model from Hugging Face's Transformers library is used. This model is chosen for its ability to handle multiple language pairs effectively, providing high-quality translations across many languages.

### Why `Helsinki-NLP/opus-mt-multi`?

The `Helsinki-NLP/opus-mt-multi` model is a robust and versatile translation model that supports a wide range of language pairs. It is built on the MarianMT architecture, which is optimized for efficient translation with high accuracy. This model is particularly suitable for applications requiring translation between less commonly paired languages, making it ideal for this multi-language translator project.

## Languages Used in the Project

The project supports translation between the following languages:

1. English (en)
2. French (fr)
3. German (de)
4. Spanish (es)

## Speech to Text Technique

We use the Google Web Speech API for the speech to text conversion. This API is chosen due to its high accuracy, ease of use, and support for a wide range of languages.

## Video Demonstration

You can view a video demonstration of the project 

https://github.com/vibhorjoshi/multi_language_app/assets/105739194/9075caa8-330a-4f3f-a5b0-e77a244fc5e5


## How to Run This Project

### Prerequisites

- Python 3.7+
- `git` installed on your machine
- `ffmpeg` installed on your machine

### Steps to Set Up and Run the Project

1. **Clone the Repository**

    ```bash
    git clone <https://github.com/vibhorjoshi/multi_language_app/edit/main>
    cd multi_language_app
    ```

2. **Create and Activate a Virtual Environment**

    On macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    On Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install the Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install `ffmpeg`**

    On Ubuntu/Debian:
    ```bash
    sudo apt-get update
    sudo apt-get install ffmpeg
    ```

    On macOS (with Homebrew):
    ```bash
    brew install ffmpeg
    ```

    On Windows:
    - Download `ffmpeg` from the [official website](https://ffmpeg.org/download.html).
    - Follow the instructions to add `ffmpeg` to your system's PATH.

5. **Run the Streamlit App**

    ```bash
    streamlit run app.py
    ```

## Project Structure

multi_language_app/

│
├── app.py

├── translator.py

├── speech_recog.py

├── requirements.txt

├── venv/ # Virtual environment directory
│
└── audio/ # Directory to store audio files for speech recognition


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


