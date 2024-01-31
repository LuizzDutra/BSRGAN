import io
import json
import os
import glob
import main_test_bsrgan as inference
import numpy as np
import cv2


from flask import Flask, jsonify, request, make_response


app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return jsonify({'msg' : 'Try POSTing to the /predict endpoint with an RGB image attachment'})


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if request.files is not None:
            image_list = []
            for f in request.files:
                #read image file string data
                filestr = request.files[f].read()
                #convert string data to numpy array
                img = np.fromstring(filestr, np.uint8)
                # convert numpy array to image
                image_list.append((f, img))

            results = inference.main(image_list)
            img = results[0][1]
            if img.ndim == 3:
                img = img[:, :, [2, 1, 0]]
            img = cv2.imencode(ext='.png', img=img)[1]
            img_bytes = img.tobytes()

            response = make_response(img_bytes)
            response.headers.set('Content-Type', 'image/png')

            return response
        
        else:
            return {'msg': "not received"}

@app.route('/test', methods=['GET'])
def test():
    if request.method == 'GET':
        print("getted")
        return {'msg': "received"}

if __name__ == '__main__':
    app.run()
