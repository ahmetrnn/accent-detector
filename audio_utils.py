import urllib.request
import subprocess
import os


import yt_dlp

def download_youtube_video(url, output_path="output/video.mp4"):
    os.makedirs("output", exist_ok=True)

    print(f"Downloading YouTube video with yt-dlp: {url}")
    
    try:
        result = subprocess.run([
            "yt-dlp",
            "-f", "ba[ext=m4a]/bestaudio/best",
            "--merge-output-format", "mp4",
            "-o", output_path,
            url
        ], capture_output=True, text=True, timeout=300)

        if result.returncode != 0:
            print("yt-dlp stdout:", result.stdout)
            print("yt-dlp stderr:", result.stderr)
            raise RuntimeError(f"yt-dlp failed with code {result.returncode}: {result.stderr}")
        
        return output_path  # ✅ Eksik olan kısım
    
    except FileNotFoundError:
        raise RuntimeError("yt-dlp not found. Make sure it's installed and in PATH")
    except subprocess.TimeoutExpired:
        raise RuntimeError("yt-dlp timed out")

def download_video(url: str, output_path: str = "output/video.mp4") -> str:
    print(f"Downloading video from: {url}")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    urllib.request.urlretrieve(url, output_path)
    size = os.path.getsize(output_path)
    print(f"Video downloaded: {output_path} ({size} bytes)")
    if size < 100000:  
        raise Exception("Downloaded file too small or invalid.")
    return output_path

def extract_audio(video_path: str, audio_output: str = "output/audio.wav") -> str:
    print("Extracting audio")
    os.makedirs(os.path.dirname(audio_output), exist_ok=True)
    command = [
        "ffmpeg", "-y", "-i", video_path,
        "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2",
        audio_output
    ]
    subprocess.run(command, check=True)
    print(f"Audio extracted to {audio_output}")
    return audio_output