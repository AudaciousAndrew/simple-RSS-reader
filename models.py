class Feed:
  db_id: int

  def __init__(self, title: str, link: str):
    self.link = link
    self.title = title

from time import struct_time


class Post:
  def __init__(self, post_id: str, published: struct_time, title: str, summary: str):
    self.post_id = post_id
    self.published = published
    self.title = title
    self.summary = summary
