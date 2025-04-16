from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import speech
from pydub import AudioSegment
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '✅ Speech-to-Text API is running! Use POST /transcribe to upload audio.'

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    # Get selected language (default: English US)
    language_code = request.form.get('language', 'en-US')

    try:
        original_path = '/tmp/' + file.filename
        file.save(original_path)

        # Convert to WAV (LINEAR16)
        audio = AudioSegment.from_file(original_path)
        wav_path = '/tmp/converted.wav'
        audio = audio.set_frame_rate(16000).set_channels(1)
        audio.export(wav_path, format='wav')

        client = speech.SpeechClient()
        with open(wav_path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=language_code,
        )

        response = client.recognize(config=config, audio=audio)

        transcription = ""
        for result in response.results:
            transcription += result.alternatives[0].transcript + " "

        os.remove(original_path)
        os.remove(wav_path)

        return jsonify({'transcription': transcription.strip()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)