import openai
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()



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

transcribe()