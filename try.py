from flask import Flask, render_template, request, jsonify, redirect
import os,base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        img = request.form['file'] .split(',')[1]
        img_byte = base64.decodebytes(img.encode())
        f = open('hhh.jpg','wb')
        f.write(img_byte)
        f.close()
        return render_template('index.html')
    

if __name__ == '__main__':
     # Set the port of the server
    PORT = int(os.getenv('VCAP_APP_PORT', '5050'))
    # Set thte IP address of the server
    HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
    app.run(host=HOST, port=PORT)