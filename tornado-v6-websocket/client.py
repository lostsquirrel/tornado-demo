# coding=utf-8
from tornado.websocket import websocket_connect


def test_web_socket(url):
    conn = yield websocket_connect(url)
    while True:
        msg = yield conn.read_message()
        if msg is None:
            break
        else:
            print(msg)
        # Do something with msg


if __name__ == '__main__':
    url = 'ws:127.0.0.1:8888'
    test_web_socket(url)
