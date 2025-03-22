from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import speech_recognition as sr

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return jsonify({'error': '未找到文件部分'}), 400
    
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': '未选择文件'}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # 语音识别
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="zh-CN")
            return jsonify({'text': text}), 200
    except Exception as e:
        return jsonify({'error': f"语音识别错误: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)