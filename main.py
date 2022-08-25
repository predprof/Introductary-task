import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def jokes():
    api_key = "74326d539da14302931e141df4fc64f7"
    # param = jokes
    r_jokes = requests.get(f"https://api.humorapi.com/jokes/random?api-key={api_key}")
    r_memes = requests.get(f"https://api.humorapi.com/memes/random?api-key={api_key}")
    r_gifs = requests.get(f"https://api.humorapi.com/gif/search?query=dog&number=3&api-key={api_key}")
    # print(jokes.text)
    data_jokes = json.loads(r_jokes.text)
    data_memes = json.loads(r_memes.text)
    data_gifs = json.loads(r_gifs.text)

    joke = data_jokes['joke']
    meme = data_memes['url']
    gif = data_gifs['images']['url']

    return render_template('index.html', joke=joke, meme=meme, gif=gif)

app.run(debug=True)
