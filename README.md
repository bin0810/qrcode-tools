# qrcode-tools
a simple tool is dev by python-flask for scan QR code and QR code recognition

# Screenshots
![image](https://github.com/bin0810/qrcode-tools/assets/122599011/877df407-7ae9-4cdc-b950-cd23189b2756)

# Quick Start

**Github**
```sh
$ git clone https://github.com/bin0810/qrcode-tools.git
$ cd qrcode-tools
$ pip install -r requirements.txt
$ python app.py
```

**Docker**
```sh
$ git clone https://github.com/bin0810/qrcode-tools.git
$ cd qrcode-tools
$ docker build -t bin/qrcode-tools:1.0 .
$ docker run -it -d --name qrcode-tools -v /home/qr_code/static:/qr_scan/static -p 5000:5000 --restart=always  bin/qrcode-tools:1.0
```


