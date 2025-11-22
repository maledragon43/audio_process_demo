# Audio Transcription Demo

A simple web application that records audio from your microphone and transcribes it to text using OpenAI's Whisper API.

## Features

- 🎤 Record audio directly from your browser's microphone
- 🔊 Real-time audio visualization
- 📝 Automatic transcription using OpenAI Whisper API
- 🎨 Modern, responsive UI

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask server:**
   ```bash
   python app.py
   ```

3. **Open your browser:**
   Navigate to `http://localhost:5000`

## Usage

1. Click "Start Recording" to begin capturing audio from your microphone
2. Speak into your microphone
3. Click "Stop & Transcribe" when you're done
4. Wait for the transcription to appear

## Requirements

- Python 3.7+
- Modern web browser with microphone access
- OpenAI API key (already configured in the code)

## Notes

- The application uses OpenAI's Whisper-1 model for transcription
- Audio is recorded in WebM format
- Make sure to allow microphone access when prompted by your browser

