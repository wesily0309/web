from flask import render_template
from flask import Flask, render_template


    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('階段2\templates\html.html')

app.run()

