import numpy as np
from flask import Flask, request, jsonify, render_template
from model import get_output
from PIL import Image

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(name="Hello Welcome to Waste Segregation!!")

@app.route('/predict', methods=['POST'])
def predict():
    path = request.json['image']    
    prediction = get_output(path) 
    return jsonify(predict = prediction)

if __name__ == '__main__':
    app.run()