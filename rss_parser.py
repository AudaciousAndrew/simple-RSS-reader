import feedparser
from models import Feed, Post
import db_controller

def fetch_feed(url):
  feed = feedparser.parse(url)
  print (feed.feed.keys())

  feed_id = db_controller.insert_feed(feed.feed)
  
  return feed_id
