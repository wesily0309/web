#from flask import render_template
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/text")
def text():
    return render_template("text")
@app.route("/home")
def home():
    return render_template('home.html')
app.run()
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def text():
    return render_template('text.html')

app.run()