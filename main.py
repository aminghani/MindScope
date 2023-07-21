from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
from utils.load_models import get_emotion, summarize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form['text']

    result = get_emotion(text)

    return jsonify(result=result)
    
@app.route('/emotion_detection', methods=['GET'])
def emotion_detection_page():
    return render_template('emotion_detection_page.html')


@app.route('/text_summarization', methods=['GET'])
def summarize_page():
    return render_template('summarize_page.html')

@app.route('/process_summarize', methods=['POST'])
def process_summarize():
    text = request.form['text']
    result = summarize(text)
    result = result[0]['summary_text']
    print(f"result ===> {result}")
    return jsonify(result=result)

if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()