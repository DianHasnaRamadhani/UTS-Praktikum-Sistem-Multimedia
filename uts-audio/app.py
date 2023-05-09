import os
import speech_recognition as sr
from pydub import AudioSegment
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET' ,'POST'])
def upload():

    file = request.files['file']
    filename = file.filename
    file_path = os.path.join('uploads', filename)
    file.save(file_path)
    sound_path = os.path.join('uploads', filename)
    sound = AudioSegment.from_file(sound_path)
    sound = sound.set_frame_rate(16000)
    sound.export('compressed_' + filename, format='wav')
    
    # Transkripsi file audio menggunakan SpeechRecognition
    r = sr.Recognizer()
    with sr.AudioFile('compressed_' + filename) as source:
        audio_data = r.record(source)
    text = r.recognize_google(audio_data, language="id-ID", key=None)


    return render_template('index.html', text = text)