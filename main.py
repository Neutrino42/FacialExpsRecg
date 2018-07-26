from flask import Flask, render_template, request, jsonify, redirect
import os
import json
import base64
import json
from watson_developer_cloud import VisualRecognitionV3



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/imageProcess', methods=['POST'])
def image_process():
    data = json.loads(request.get_data())
    img = data["file"].split(',')[1]
    img_byte = base64.decodebytes(img.encode())
    f = open('./static/image/snapshot.jpg', 'wb')
    f.write(img_byte)
    f.close()

    # Using IBM watson Visual Recognition Model
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',  # version
        iam_api_key='pBwT3fGN4RBkPGyHhlI5mauax570lg3tjjP68bCdT4jJ')  # your API key

    with open('./static/image/snapshot.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            parameters=json.dumps({
                'classifier_ids': ["food"]
            }))
    result = json.dumps(classes, indent=2)
    expression_result = eval(result)["images"][0]["classifiers"][0]["classes"][0]["class"]

    return jsonify({'result': expression_result})


if __name__ == '__main__':
    # Set the port of the server
    PORT = int(os.getenv('VCAP_APP_PORT', '5050'))
    # Set thte IP address of the server
    HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
    app.run(host=HOST, port=PORT)