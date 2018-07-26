from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/static/photo/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def hello_world():
    return render_template('Capture.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/receive_photo',methods = ['POST'])
def receive_pthoto():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
    return render_template('Capture.html')

if __name__ == '__main__':
    # Set the port of the server
    PORT = int(os.getenv('VCAP_APP_PORT', '5050'))
    # Set thte IP address of the server
    HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
    app.run(host=HOST, port=PORT)
