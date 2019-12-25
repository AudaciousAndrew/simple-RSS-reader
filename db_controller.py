import sqlite3
import time
from typing import Optional, List
from models import Feed, Post

def create_connection():
  return sqlite3.connect('lab6.db')


def init(script_names: List[str]):
  cursor = create_connection().cursor()

  cursor.execute("""create table if not exists feeds (
    id integer primary key autoincrement,
    title text not null,
    url text not null
  );""") 

  cursor.execute("""create table if not exists posts (
    id integer primary key autoincrement,
    feed_id integer not null,
    date_published integer,
    title text,
    summary text,
    foreign key(feed_id) references feeds(id)
  );""")



init(['feed', 'post'])


def get_feed_by_id(feed_id: int) -> Feed:
  cursor = create_connection().cursor()
  cursor.execute('SELECT * FROM FEED WHERE ID = ?', (feed_id,))

  return map_feed(cursor.fetchone())


def get_all_feeds() -> List[Feed]:
  cursor = create_connection().cursor()
  cursor.execute('SELECT * FROM FEED')

  result = []
  for fetched_record in cursor.fetchall():
    feed = map_feed(fetched_record)
    result.append(feed)

  return result


def map_feed(fetched_record):
  feed = Feed(fetched_record[1], fetched_record[2])
  feed.db_id = fetched_record[0]
  return feed


def save_feed(feed: Feed) -> int:
  connection = create_connection()

  with connection:
    cursor = connection.cursor()
    cursor.execute('INSERT INTO FEED VALUES (NULL, ?, ?)', (feed.title, feed.link))

  return cursor.lastrowid


def get_feed_id_by_link(link: str) -> Optional[int]:
  return value_or_none('SELECT ID FROM FEED WHERE LINK = ?', (link,))


def value_or_none(query, args):
  cursor = create_connection().cursor()
  cursor.execute(query, args)
  fetched = cursor.fetchone()

  return None if fetched is None else fetched[0]


def save_posts(feed_id: int, posts: List[Post]):
  connection = create_connection()

  with connection:
    for post in posts:
      connection.execute('INSERT INTO POST VALUES (NULL, ?, ?, ?, ?, ?)',
                          (post.post_id, feed_id, time.mktime(post.published), post.title, post.summary))


def get_posts_count(feed_id: int) -> int:
  return value_or_none('SELECT COUNT(*) FROM POST WHERE FEED_ID = ?', (feed_id,))


def get_posts_by_feed_id(feed_id: int, page: int, limit: int) -> List[Post]:
  cursor = create_connection().cursor()
  cursor.execute('SELECT POST_ID, PUBLISHED, TITLE, SUMMARY FROM POST WHERE FEED_ID = ? '
                  'ORDER BY PUBLISHED DESC LIMIT ? OFFSET ?',
                  (feed_id, limit, (page - 1) * limit))

  result = []
  for fetched_record in cursor.fetchall():
      feed = map_post(fetched_record)
      result.append(feed)

  return result


def map_post(fetched_record) -> Post:
  return Post(fetched_record[0], time.localtime(int(fetched_record[1])), fetched_record[2], fetched_record[3])


def get_last_post_id(feed_id: int) -> str:
  return value_or_none('SELECT POST_ID FROM POST WHERE FEED_ID = ? ORDER BY PUBLISHED DESC LIMIT 1', (feed_id,))
