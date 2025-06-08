import whisper

model = whisper.load_model("tiny")
def transcribe_audio(audio_path: str) -> dict:
    print(f"🔍 Transcribing audio: {audio_path}")
    result = model.transcribe(audio_path)

    transcript = result.get("text", "")
    language = result.get("language", "unknown")

    print("✅ Transcription complete.")
    print("🌍 Detected language:", language)

    return {
        "text": transcript,
        "language": language
    }