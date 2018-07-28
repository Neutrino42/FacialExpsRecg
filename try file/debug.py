from flask import Flask, render_template, request, jsonify, redirect
import os,base64
import json
from watson_developer_cloud import VisualRecognitionV3

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('debug.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # img = request.form['file'] .split(',')[1]
        img = request.get_json('file')
        img_byte = base64.decodebytes(img['file'].split(',')[1].encode())
        f = open('hhh.jpg','wb')
        f.write(img_byte)
        f.close()        
    return classfication()

def classfication():
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_api_key='pBwT3fGN4RBkPGyHhlI5mauax570lg3tjjP68bCdT4jJ')

    with open('./hhh.jpg', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            parameters = json.dumps({
                'classifier_ids': ["food"]
            }))

    classfy_dic = eval(json.dumps(classes, indent=2))
    results = classfy_dic["images"][0]["classifiers"][0]["classes"][0]["class"]
    # print('hhh')
    # return jsonify((json.dumps(classes, indent=2)))
    # print(results)
    # return jsonify(json.dumps(classes, indent=2))
    return jsonify({'result':results})

    

if __name__ == '__main__':
     # Set the port of the server
    PORT = int(os.getenv('VCAP_APP_PORT', '5050'))
    # Set thte IP address of the server
    HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
    app.run(host=HOST, port=PORT)