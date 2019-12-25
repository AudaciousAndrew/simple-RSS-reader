from flask import Flask, render_template, request, redirect, url_for
import rss_parser
import db_controller

app = Flask(__name__)

PAGE_SIZE = 10

rss_parser.fetch_feed("https://www.reddit.com/r/Python/.rss")

@app.route("/")
def index():
    feeds = db_controller.get_all_feeds()
    return render_template("index.html" , feeds = feeds)


@app.route("/import", methods=["POST"])
def import_feed():
    link = request.form.get("link")
    rss_parser.parse_feed(link)

    return redirect(url_for("index"))


@app.route("/feed/<feed_id>")
def get_feed(feed_id):
    page = request.args.get('page', default=1, type=int)

    feed = db_controller.get_feed_by_id(feed_id)
    posts = db_controller.get_posts_by_feed_id(feed_id, page, PAGE_SIZE)
    total = db_controller.get_posts_count(feed_id)

    return render_template("feed.html", feed=feed, feed_id=feed_id, posts=posts, page=page,
                           pages_count=ceil(total / PAGE_SIZE))


@app.route("/feed/<feed_id>", methods=["POST"])
def refresh_feed(feed_id):
    feed = db_controller.get_feed_by_id(feed_id)
    rss_parser.parse_feed(feed.link)

    return redirect(f"/feed/{feed_id}")


def format_datetime(value):
    return time.strftime('%Y-%m-%d %H:%M:%S', value)


app.jinja_env.filters['format_time'] = format_datetime


if __name__ == "__main__":
    app.run(debug=True)
