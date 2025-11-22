# Audio Transcription Demo

A simple web application that records audio from your microphone and transcribes it to text using OpenAI's Whisper API.

## Features

- 🎤 Record audio directly from your browser's microphone
- 🔊 Real-time audio visualization
- 📝 Automatic transcription using OpenAI Whisper API
- 🎨 Modern, responsive UI

## Setup

1. **Create a `.env` file:**
   Create a file named `.env` in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask server:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   Navigate to `http://localhost:5000`

## Usage

1. Click "Start Recording" to begin capturing audio from your microphone
2. Speak into your microphone
3. Click "Stop & Transcribe" when you're done
4. Wait for the transcription to appear

## Requirements

- Python 3.7+
- Modern web browser with microphone access
- OpenAI API key (configure in `.env` file)

## Notes

- The application uses OpenAI's Whisper-1 model for transcription
- Audio is recorded in WebM format
- Make sure to allow microphone access when prompted by your browser

