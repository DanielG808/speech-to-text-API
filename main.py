from flask import Flask, request
import openai
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the speech-to-text flask app!"

@app.route("/transcribe/<file-path>")
def transcribe():
    API_KEY = os.getenv("API_KEY")
    media_file = open("./assets/test-recording.m4a", "rb")

    response = openai.Audio.transcribe(
        api_key=API_KEY,
        model="whisper-1",
        file=media_file,
        response_format="text"
    )
    print(response)
    return response

if __name__ == "__main__":
    app.run(debug=True)
