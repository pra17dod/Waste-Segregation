import numpy as np
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return 

@app.route('/predict', methods=['POST'])
def predict():

    return 

if __name__ == "__main__":
    app.run(debug=True)