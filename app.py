
from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


@app.route("/")
def home():
    count = redis_client.incr("visits")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Visitor Counter</title>
    </head>
    <body>
        <h1>Welcome to My Visitor Counter version 2</h1>
        <p>Hello! 👋</p>
        <p>This page has been visited <strong>{count}</strong> times.</p>
        <p>Powered by Flask and Redis.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)