import sqlite3
import feedparser


conn = sqlite3.connect('lab6.db');

print ("Opened database successfully");
# https://www.reddit.com/r/Python/.rss
# https://habr.com/ru/rss/interesting/
NewsFeed = feedparser.parse("https://www.reddit.com/r/Python/.rss");

print (f"Number of RSS posts :{len(NewsFeed.entries)}");

entry = NewsFeed.entries[1];

print (entry.keys());
print (f"Post Title :{entry.title}");