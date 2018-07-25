from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('Capture.html')


if __name__ == '__main__':
    # Set the port of the server
    PORT = int(os.getenv('VCAP_APP_PORT', '5050'))
    # Set thte IP address of the server
    HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
    app.run(host=HOST, port=PORT)
