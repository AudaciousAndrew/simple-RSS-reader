class Feed:
    def __init__(self, id, title, url):
      self.id = id
      self.title = title
      self.url = url

class Post:
    def __init__(self, id, feed_id, date_published, title, summary):
      self.id = id
      self.feed_id = feed_id
      self.date_published = date_published
      self.title = title
      self.summary = summary