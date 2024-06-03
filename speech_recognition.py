import speech_recognition as sr
from pydub import AudioSegment
import os

def extract_audio_from_video(video_file, audio_file):
    video = AudioSegment.from_file(video_file, format="mp4")
    video.export(audio_file, format="wav")

def recognize_speech(file_path):
    # Check if the file is a video
    if file_path.lower().endswith(".mp4"):
        audio_file = file_path.replace(".mp4", ".wav")
        extract_audio_from_video(file_path, audio_file)
    else:
        audio_file = file_path
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    file_path = "audio/20230103_013922.mp4"  # Provide the path to your audio or video file
    text = recognize_speech(file_path)
    print(f"Recognized text: {text}")
