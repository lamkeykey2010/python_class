from flask import Flask, render_template
import urllib.request #python 3.6 does not have the urllib2, so I need to use another one
import json

app = Flask(__name__)


@app.route('/')
def index():

    response        = urllib.request.urlopen('https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json')
    data  = json.load(response)

    pokemon_index         = data["pokemon"]
    pokemon_records = []

    for pokemon in pokemon_index:
        record_tuple = (pokemon["num"], pokemon["name"], pokemon["type"])
        pokemon_records.append(record_tuple)

    return render_template('index.html', records=pokemon_records)


if __name__ == '__main__':
    # Starts the Flask application server
    app.run(debug=True)
