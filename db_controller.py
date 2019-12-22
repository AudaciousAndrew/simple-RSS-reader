import sqlite3
import models

conn = sqlite3.connect('lab6.db');
cur = conn.cursor()

#Creating tables for feeds and posts
cur.execute("""create table if not exists feeds (
	id integer primary key autoincrement,
  title text not null,
  url text not null
);""") 

cur.execute("""create table if not exists posts (
	id integer primary key autoincrement,
  feed_id integer not null,
  date_published integer,
  title text,
  summary text,
  foreign key(feed_id) references feeds(id)
);""")

cur.close()
conn.close()


def insert_feed(feed):
  conn = sqlite3.connect('lab6.db')
  with conn:
    cur = conn.cursor()
    cur.execute("insert into feeds(title, url) values(?, ?)", (feed.title, feed.link))

  return cur.lastrowid
