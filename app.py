from flask import Flask, request, render_template
from textblob import TextBlob
def sentiment(x):
    return TextBlob(x).sentiment.polarity
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def get_val():
    name = request.form['text']

    return render_template('pass.html', n = sentiment(name))

app.run(debug = True)