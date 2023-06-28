
from flask import Flask, request, render_template, send_file, jsonify
import argparse
import qrcode
from PIL import Image
import os
import random
import requests

link = ''
name = ''
message = ""
file_location = ''


parser = argparse.ArgumentParser(description='Flask Application')
parser.add_argument('--host', type=str, default='0.0.0.0', help='Host IP address')
parser.add_argument('--port', type=int, default=80, help='Port number')
args = parser.parse_args()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-link', methods=['POST'])
def get_link():
    global link, name
    link = request.form.get('link_get')
    name = request.form.get('name_get')
    x = requests.head(link)
    if x.status_code != 404:
        create_code(link)
    else:
        print("not available")
    return link
def create_code(link):
    qr_code = qrcode.make(link)
    global file_location
    if name != '':
        file_location = 'Uploaded/' + name + '.png'
        qr_code.save(file_location)
        print(file_location)
        get_alert_message()
@app.route('/get-alert-message')
def get_alert_message():
    global message
    message = ''
    if name != '' and link != '':
        message = "QR created successfully!click on ShowQR to view"
    else:
        message = "Invalid Credentials"
    return jsonify(message=message)

@app.route('/image')
def get_image():

    filename = file_location
    print(filename)
    return send_file(filename, mimetype='image/png')

@app.route('/download-output', methods=['GET'])
def download_output():
    print(file_location)
    return send_file(file_location, as_attachment=True)

if __name__ == '__main__':
    app.run(host=args.host, port=args.port, debug=True)
