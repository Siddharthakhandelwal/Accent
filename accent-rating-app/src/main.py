from unittest import result
import gdown
import requests
import assemblyai as aai
import os
from utils import convert_mp4_to_mp3, get_file_id

def assembly(audio_file):
    aai.settings.api_key = "9195d7c4cdec43238006f64f72d01b1c"
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)
    transcript = aai.Transcriber(config=config).transcribe(audio_file)

    if transcript.status == "error":
        print("Error:", transcript.error)
        return None
    else:
        return transcript.text[:1000]  # Return first 1000 characters of the transcript

def create_post():
    transcript_text = assembly("Marc_Kervens_Simeon_2025-08-02_21-14-07_Video.mp3")
    url = "https://thefluentme.p.rapidapi.com/post"

    payload = {
        "post_language_id": "22",
        "post_title":"first post",  # First 60 characters of the transcript as title
        "post_content":"This is an example post. The post can be between three and 1000 characters long."
    }
    headers = {
        "x-rapidapi-key": "8cc9f78fb1msh7bc3e2f14815ce2p1e2b6cjsn6234c893bf06",
        "x-rapidapi-host": "thefluentme.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
    return response.json()["post_id"]

def get_result(post_id):

    url = f"https://thefluentme.p.rapidapi.com/score/{post_id}"

    querystring = {"scale":"90"}

    payload = { "audio_provided": "https://storage.googleapis.com/thefluentme01.appspot.com/audio/test/example_user_recording.wav" }
    headers = {
        "x-rapidapi-key": "8cc9f78fb1msh7bc3e2f14815ce2p1e2b6cjsn6234c893bf06",
        "x-rapidapi-host": "thefluentme.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    print(response.json())
    return response.json()

def main():
    # download_url = "https://drive.google.com/file/d/1o63ILg3-CUEx-a7B2hglW-YQTP81_gl9/view?usp=drive_link"  # Replace with your Google Drive link
    # file_id = get_file_id(download_url)
    # print("Extracted File ID:", file_id)
    # if file_id:
    id=create_post()
    result = get_result(id)
    print(result)
if __name__ == "__main__":
    main()