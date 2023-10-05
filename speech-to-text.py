import openai
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

API_KEY = os.getenv("API_KEY")

model_id = "whisper-1"

media_file_path = "./assets/test-recording.m4a"
media_file = open(media_file_path, "rb")

response = openai.Audio.transcribe(
    api_key=API_KEY,
    model=model_id,
    file=media_file,
    response_format="text"
)

print(response)