import sqlite3
import feedparser
from flask import Flask, render_template, request, redirect, url_for
import rss_parser

app = Flask(__name__)

rss_parser.fetch_feed("https://www.reddit.com/r/Python/.rss")
'''
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feed")
def feed():
    return render_template("feed.html")


if __name__ == "__main__":
    app.run(debug=True)
'''