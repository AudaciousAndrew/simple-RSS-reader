import sqlite3
import feedparser
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

conn = sqlite3.connect('lab6.db');

print ("Opened database successfully");
# https://www.reddit.com/r/Python/.rss
# https://habr.com/ru/rss/interesting/
NewsFeed = feedparser.parse("https://www.reddit.com/r/Python/.rss");

print (f"Number of RSS posts :{len(NewsFeed.entries)}");

entry = NewsFeed.entries[1];

print (entry.keys());
print (f"Post Title :{entry.title}");

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feed")
def feed():
    return render_template("feed.html")


if __name__ == "__main__":
    app.run(debug=True)
