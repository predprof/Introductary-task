import json
import requests
from flask import Flask, render_template
from flask_pymongo import PyMongo
import flask

app = Flask(__name__)
api_key = "74326d539da14302931e141df4fc64f7"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/jokes")
def jokes():
    r_jokes = requests.get(f"https://api.humorapi.com/jokes/random?api-key={api_key}")
    data_jokes = json.loads(r_jokes.text)
    joke = data_jokes['joke']
    return render_template('jokes.html', joke=joke)


@app.route("/memes", methods=('GET',))
def memes():
    r_memes = requests.get(f"https://api.humorapi.com/memes/random?api-key={api_key}")
    data_memes = json.loads(r_memes.text)
    meme = data_memes['url']
    return render_template('memes.html', meme=meme)


@app.route("/gif")
def gifs():
    r_gifs = requests.get(f"https://api.humorapi.com/gif/search?query=dog&number=3&api-key={api_key}")
    data_gifs = json.loads(r_gifs.text)
    gif = data_gifs['images'][0]['url']
    return render_template('gif.html', gif=gif)


# app.run(debug=True)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
