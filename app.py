
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Text_Minecraft')
def TM():
    return render_template('Text_Minecraft.html')

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')