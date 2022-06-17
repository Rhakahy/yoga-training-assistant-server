from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from setup import *

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
  app.run('127.0.0.1', 5600, debug=True, ssl_context=('cert.pem', 'key.pem'))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
  file = request.files['file']
  file.save('./input/' + file.filename.replace(' ', '_'))
  path = './input/' + file.filename.replace(' ', '_')

  return {
    'status': 'success',
    'filename': file.filename.replace(' ', '_')
  }

@app.route('/getResponse', methods=['POST', 'GET'])
def get_response():
  import requests
  import cv2
  filename = request.args.get('filename')
  path = './input/' + filename
  img = cv2.imread(path)
  # cv2.imshow('image', img)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  result = predict_pose(img)
  return result

@app.route('/getImage', methods=['POST', 'GET'])
def get_image():
  filename = request.args.get('filename')
  return send_from_directory('./input', filename)