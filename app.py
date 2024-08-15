from pytube3 import YouTube
from pydub import AudioSegment
import os
import logging


logging.basicConfig(level=logging.INFO)

def download_youtube_audio(youtube_url, output_path='output.mp3'):
    try:
        logging.info(f"Downloading audio from {youtube_url}")
        yt = YouTube(youtube_url)
        video_stream = yt.streams.filter(only_audio=True).first()
        
        if not video_stream:
            raise Exception("No audio streams available")

        downloaded_file = video_stream.download(filename="temp_audio")
        logging.info(f"Downloaded audio file: {downloaded_file}")

        # Convert the downloaded file to MP3
        logging.info(f"Converting {downloaded_file} to MP3")
        audio = AudioSegment.from_file(downloaded_file)
        audio.export(output_path, format="mp3")

        # Remove the original downloaded file
        os.remove(downloaded_file)
        logging.info(f"Audio file saved as {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")



youtube_url = 'https://www.youtube.com/watch?v=sDhjuMej_QU'  # Replace with your YouTube URL
download_youtube_audio(youtube_url)
