# English Accent Detector

This is a web-based application that detects the **English accent** of a speaker in a publicly available video. It uses **Whisper** for transcription and a keyword-based logic to infer the accent.

---

## Features

 Download video from **YouTube or direct links**
 Extract and transcribe **English speech** using OpenAI Whisper
 Detect accent based on keyword frequency and summary
 Simple web interface using **Flask + Jinja2**

---

## Installation (Local)

1. Clone the repo

```bash
git clone https://github.com/ahmetrnn/accent-detector.git
cd accent-detector
```

2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Make sure `ffmpeg` and `yt-dlp` are installed and in your PATH.

```bash
brew install ffmpeg
brew install yt-dlp
```

5. Run the app locally

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Project Structure

```
accent-detector/
│
├── app.py                      # Main Flask app
├── audio_utils.py              # Audio downloading and extraction
├── whisper_transcriber.py      # Whisper transcription logic
├── accent_detector.py          # Accent classification logic
├── templates/
│   └── index.html              # UI template
├── output/                     # Temporary video/audio storage
├── requirements.txt
```

---

## Notes

- Only English speech is supported
- Videos must be public and contain audible speech
- If a video has no sound or English, you'll get an error message

---

## Author

Built by [Ahmet Eren](https://github.com/ahmetrnn)

---

## License

MIT License – feel free to fork and improve!
