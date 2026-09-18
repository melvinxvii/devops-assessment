from app import app
from unittest.mock import patch


def test_home():
    client = app.test_client()

    with patch("app.redis_client.incr", return_value=1):
        response = client.get("/")

    assert response.status_code == 200
    assert b"Visitor Counter" in response.data