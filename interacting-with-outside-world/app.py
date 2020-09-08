import os
import shutil
from flask import Flask, send_file
import requests

app = Flask(__name__)

SECRET_KEY = os.environ['SECRET_KEY']

@app.route('/')
def gday_world():
    return "Gday World!"

@app.route('/<secretkey>')
def show_dog(secretkey):
    if SECRET_KEY == secretkey:
        r = requests.get("https://cataas.com/cat")
        with open('pic.jpeg', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        return send_file('pic.img')
    else:
        return 'Who are you?', 401
    
if __name__ == '__main__':
    app.run()