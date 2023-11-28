import os.path
import datetime
import qrcode
import cv2
import pathlib

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__, static_folder='static')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/qr/genrate', methods=['POST'])
def get_qr():
    info = request.form['info']
    if info:
        name = generate_qr(info)
        return render_template("index.html", qr_image=name, user_in=info)
    else:
        return render_template('index.html')


@app.route('/qr/upload', methods=['POST'])
def get_upload():
    if request.method == 'POST':
        qr_file = request.files.get('file')
        f_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + '.jpg'
        f_url = os.path.join(app.static_folder, 'upload', f_name)
        pathlib.Path(os.path.dirname(f_url)).mkdir(parents=True, exist_ok=True)
        qr_file.save(f_url)
        val = scan_qr(f_url)
        return render_template("index.html", info=val)
    else:
        return render_template('index.html', info="Sorry,解析失败!")


def generate_qr(msg):
    qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=10, border=4)
    qr.add_data(str(msg))
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    f_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + '.jpg'
    f_url = os.path.join(app.static_folder, 'generate', f_name)
    pathlib.Path(os.path.dirname(f_url)).mkdir(parents=True, exist_ok=True)
    img.save(f_url)
    return f_name


def scan_qr(qr_file):
    d = cv2.QRCodeDetector()
    val, _, _ = d.detectAndDecode(cv2.imread(qr_file))
    if val:
        return val


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
