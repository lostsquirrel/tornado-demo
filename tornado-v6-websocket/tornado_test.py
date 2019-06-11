# coding=utf-8

import tornado
import unittest


class TornadoTests(unittest.TestCase):

    def test_version(self):
        print(tornado.version)

        self.assertEqual('6.0.2', tornado.version)

    def test_websocket_exists(self):
        print([x for x in dir(tornado) if not x.startswith('__')])
        print(tornado.web)
        print(tornado.ioloop)
        print(tornado.websocket)


if __name__ == '__main__':
    unittest.main()
