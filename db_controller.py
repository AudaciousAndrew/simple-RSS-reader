import sqlite3

conn = sqlite3.connect('lab6.db');
cur = conn.cursor()

#Creating tables for feeds and posts
cur.execute("""create table if not exists feeds (
	id integer primary key autoincrement,
  url text not null
);""") 

cur.execute("""create table if not exists posts (
	id integer primary key autoincrement,
  feed_id integer not null,
  date_published integer,
  summary text,
  foreign key(feed_id) references feeds(id)
);""")


