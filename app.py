import os

from flask import Flask
app = Flask(__name__)

import random

def generate_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    hr = hex(r).replace("0x","")
    hg = hex(g).replace("0x","")
    hb = hex(b).replace("0x","")
    while len(hr) <= 1: hr = "0" + hr
    while len(hg) <= 1: hg = "0" + hg
    while len(hb) <= 1: hb = "0" + hb

    return "#" + hr + hg + hb



@app.route('/')
def hello():
    return open("html/index.html").read() 


@app.route('/classify/<int:value>')
def respond_color(value):
    return "you respondeded",value
        

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
