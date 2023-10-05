from flask import Flask, request
import os
import openai

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the speech-to-text flask app!"

app.route("/create-text", methods=["POST"])
def transcribe(path)
    audio_file = open(path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    return transcript

if __name__ == "__main__":
    app.run(debug=True)
