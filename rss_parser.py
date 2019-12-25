import feedparser
from models import Feed, Post
import db_controller

def fetch_feed(url):
  feed = feedparser.parse(url)
  print (feed.feed.keys())

  feed_id = db_controller.get_feed_id_by_url(url)
  if feed_id is None:
    new_feed = Feed(feed.feed.title, url)
    feed_id = db_controller.insert_feed(new_feed)

  
  return feed_id
