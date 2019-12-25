import feedparser
import db_controller

from typing import List
from models import Feed, Post


def parse_feed(link: str) -> bool:
  parsed_feed = feedparser.parse(link)
  if hasattr(parsed_feed, 'bozo_exception'):
    return False

  feed_id = db_controller.get_feed_id_by_link(link)
  if feed_id is None:
    feed = Feed(parsed_feed.feed.title, link)
    feed_id = db_controller.save_feed(feed)

  last_post_id = db_controller.get_last_post_id(feed_id)

  posts = parse_posts(parsed_feed.entries, last_post_id)
  db_controller.save_posts(feed_id, posts)


def parse_posts(posts, last_post_id: str) -> List[Post]:
  result = []
  for post in posts:
    if post.id == last_post_id:
      break
    result.append(Post(post.id, post.published_parsed, post.title, post.summary))
  
  return result