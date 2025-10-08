import requests
import assemblyai as aai
from utils import convert_mp4_to_wav_and_trim, get_file_id
import re
import gdown
import os

def upload_file_catbox(filepath):
    url = "https://catbox.moe/user/api.php"
    with open(filepath, "rb") as f:
        files = {"fileToUpload": f}
        data = {"reqtype": "fileupload"}
        response = requests.post(url, data=data, files=files)

    if response.ok:
        download_link = response.text.strip()
        print(f"✅ File uploaded: {download_link}")
        return download_link  # Direct .wav link
    else:
        print("❌ Upload failed:", response.text)
        return None


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
        "x-rapidapi-key": "b6061cbd87mshefee4c02d666d4ap14b4b9jsn43f1962dd28b",
        "x-rapidapi-host": "thefluentme.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())
    return response.json()["post_id"]

def get_result(post_id,file_url):

    audio_url = file_url
    url = f"https://thefluentme.p.rapidapi.com/score/{post_id}"

    querystring = {"scale":"90"}

    payload = { "audio_provided": audio_url }
    headers = {
        "x-rapidapi-key": "b6061cbd87mshefee4c02d666d4ap14b4b9jsn43f1962dd28b",
        "x-rapidapi-host": "thefluentme.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)
    return response.json()

def main():
    download_url = "https://drive.google.com/file/d/1_m7L2LewUwHYSNzbpfhWhxl544kQJVAX/view?usp=sharing"
    file_id = get_file_id(download_url)
    print("Extracted File ID:", file_id)
    if file_id:
        mp4_path=download_from_gdrive_by_id(file_id)
        wav_path = convert_mp4_to_wav_and_trim(mp4_path)#"Timothy_Mbiti_2025-07-26_21-42-10_Video.wav"
        print("Converted WAV Path:", wav_path)
        wav_file_url= upload_file_catbox(wav_path)
        print("Uploaded WAV File URL:", wav_file_url)
        id=create_post(wav_path)
        print("Created Post ID:", id)
        result = get_result(id,wav_file_url)
        print(result)
        os.remove(mp4_path)
        os.remove(wav_path)

if __name__ == "__main__":
    main()