from flask import Flask, request, render_template
from flask_cors import CORS
from audio_utils import download_video, download_youtube_video, extract_audio
from whisper_transcriber import transcribe_audio
from accent_detector import detect_accent
import os

app = Flask(__name__)
CORS(app)

os.makedirs("output", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("video_url")
        try:
            if "youtube.com" in url or "youtu.be" in url:
                video_path = download_youtube_video(url)
            else:
                video_path = download_video(url)

            audio_path = extract_audio(video_path)
            transcript_data = transcribe_audio(audio_path)

            if not transcript_data["text"].strip():
                result = {"error": "Transcript is empty. Try a different video."}
            elif transcript_data["language"] != "en":
                result = {"error": "Detected language is not English."}
            else:
                accent = detect_accent(transcript_data["text"])
                result = {
                    "transcript": transcript_data["text"],
                    "accent": accent["accent"],
                    "confidence": accent["confidence"],
                    "summary": accent["summary"]
                }
        except Exception as e:
            result = {"error": f"{type(e).__name__}: {str(e)}"}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)