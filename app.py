from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI
import os
import tempfile

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = OpenAI(api_key="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")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    try:
        # Check if audio file is in the request
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
        
        audio_file = request.files['audio']
        
        # Save audio to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as tmp_file:
            audio_file.save(tmp_file.name)
            tmp_path = tmp_file.name
        
        try:
            # Transcribe using OpenAI Whisper API
            with open(tmp_path, 'rb') as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language="en"  # Optional: specify language
                )
            
            transcription_text = transcript.text
            
            return jsonify({
                'success': True,
                'transcription': transcription_text
            })
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Disable reloader on Windows to avoid socket errors
    app.run(debug=True, use_reloader=False, port=5000)

