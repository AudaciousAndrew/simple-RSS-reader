import sqlite3
import feedparser

import rss_parser
import db_controller

conn = sqlite3.connect('lab6.db');

rss_parser.fetch_feed("https://www.reddit.com/r/Python/.rss")
#rss_parser.fetch_feed("https://habr.com/ru/rss/interesting/")


