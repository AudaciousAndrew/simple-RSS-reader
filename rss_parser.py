import feedparser

def fetch_feed(url):
  feed = feedparser.parse(url)
  print (f"Number of RSS posts :{len(feed.entries)}")

  entry = feed.entries[5]

  print (entry.keys())
  print (f"Post Title :{entry.title}")
  print (f"Post :{entry.updated_parsed}")
  
