import os

from flask import Flask
app = Flask(__name__)

import random
import psycopg2


def create_conn():
    conn = None
    if os.environ.has_key("DATABASE_URL"):
        username = os.environ["DATABASE_URL"].split(":")[1].replace("//","")
        password = os.environ["DATABASE_URL"].split(":")[2].split("@")[0]
        host = os.environ["DATABASE_URL"].split(":")[2].split("@")[1].split("/")[0]
        dbname = os.environ["DATABASE_URL"].split(":")[2].split("@")[1].split("/")[1] 
        conn = psycopg2.connect(dbname=dbname, user=username, password=password, host=host) 
    return conn


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

    return hr + hg + hb

@app.route("/js/jquery.min.js")
def jquery():
    return open("js/jquery.min.js").read()

@app.route('/')
def hello():
    return open("html/index.html").read()

@app.route("/style.css")
def stylesheet():
    return open("html/style.css").read()

@app.route("/beige.js")
def beigejs():
    return open("html/beige.js").read().replace("ff00ff",generate_color()) 

@app.route("/getcolor")
def givemeacolor():
    return generate_color()

@app.route('/classify/<int:value>/<color>')
def respond_color(value, color):
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO colors VALUES (%s,%s)", (color, str(value)))    
    conn.commit()
    return "yup"
        

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
