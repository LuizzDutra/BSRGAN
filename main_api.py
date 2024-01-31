import io
import json
import os

import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request
from ultralytics import YOLO
from ultralytics.engine.results import Probs, Results
import numpy as np


app = Flask(__name__)
model = YOLO("yolov8l-cls.pt")


@app.route('/', methods=['GET'])
def root():
    return jsonify({'msg' : 'Try POSTing to the /predict endpoint with an RGB image attachment'})


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file is not None:
            pass

if __name__ == '__main__':
    app.run()
