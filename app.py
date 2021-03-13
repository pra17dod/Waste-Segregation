import numpy as np
from flask import Flask, request, jsonify, render_template
from model import get_output
app = Flask(__name__)

@app.route("/")
def home():
    return 

@app.route('/predict', methods=['POST'])
def predict():
    return  get_output()
 

if __name__ == "__main__":
    app.run(debug=True)