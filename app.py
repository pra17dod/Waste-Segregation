import numpy as np
from flask import Flask, request, jsonify, render_template
from model import get_output
from PIL import Image
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def home():
    return jsonify(name="What's your name??")

@app.route('/predict', methods=['POST'])
def predict():
    path = request.json['image']    
    prediction = get_output(path) 
    return jsonify(predict = prediction)

if __name__ == '__main__':
    app.run()