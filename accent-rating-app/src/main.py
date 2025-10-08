from unittest import result
import requests
import assemblyai as aai
import os
from utils import convert_mp4_to_wav_and_trim, get_file_id
import re
import gdown

def upload_gdrive_wav(wav_path):
    pass

def download_from_gdrive_by_id(file_id, output=None):
    """
    Download file from Google Drive using file ID.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    try:
        downloaded = gdown.download(url, output=output, quiet=False)
        return downloaded
    except Exception as e:
        print("❌ gdown error:", e)
        return None


def assembly(audio_file):
    aai.settings.api_key = "9195d7c4cdec43238006f64f72d01b1c"
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)
    transcript = aai.Transcriber(config=config).transcribe(audio_file)

    if transcript.status == "error":
        print("Error:", transcript.error)
        return None
    else:
        return transcript.text[:20]  # Return first 1000 characters of the transcript

def create_post(wav_path):
    transcript_text = assembly(wav_path)
    print("Transcript Text:", transcript_text)
    url = "https://thefluentme.p.rapidapi.com/post"

    payload = {
        "post_language_id": "22",
        "post_title":"first post",  # First 60 characters of the transcript as title
        "post_content": transcript_text,  # Full transcript as content
    }
    headers = {
        "x-rapidapi-key": "8cc9f78fb1msh7bc3e2f14815ce2p1e2b6cjsn6234c893bf06",
        "x-rapidapi-host": "thefluentme.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
    return response.json()["post_id"]

def get_result(post_id,file_id):
    
    audio_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    url = f"https://thefluentme.p.rapidapi.com/score/{post_id}"

    querystring = {"scale":"90"}

    payload = { "audio_provided": audio_url }
    headers = {
        "x-rapidapi-key": "8cc9f78fb1msh7bc3e2f14815ce2p1e2b6cjsn6234c893bf06",
        "x-rapidapi-host": "thefluentme.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    print(response.json())
    return response.json()

def main():
    download_url = "https://drive.google.com/file/d/1o63ILg3-CUEx-a7B2hglW-YQTP81_gl9/view?usp=drive_link"  
    file_id = get_file_id(download_url)
    print("Extracted File ID:", file_id)
    if file_id:
        mp4_path=download_from_gdrive_by_id(file_id)
        wav_path = convert_mp4_to_wav_and_trim(mp4_path)
        id=create_post(wav_path)
        wav_file_url= upload_gdrive_wav(wav_path)
        wav_file_id= get_file_id(wav_file_url)
        result = get_result(id,wav_file_id)
        print(result)
        
if __name__ == "__main__":
    main()