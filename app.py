from flask import Flask, render_template
import os

app = Flask(__name__)

def read_file(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "תוכן לא נמצא"
    
    
@app.route('/')
def index():
    title = read_file("text_files/title.txt")
    intro = read_file("text_files/intro.txt")
    return render_template('index.html', title=title, intro=intro)

@app.route('/donate')
def donate():
    donate = read_file("text_files/donate.txt")
    return render_template('donate.html', donate=donate)

@app.route('/summary')
def summary():
    summary = read_file("text_files/summary.txt")
    return render_template('summary.html', summary=summary)
