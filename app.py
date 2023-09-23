"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
import random
from histogram_oop import Histogram


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
hist = Histogram("./data/dracula.txt", order=3)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    phrase = hist.get_random_phrase("markov")
    return render_template("index.html", phrase=phrase)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
