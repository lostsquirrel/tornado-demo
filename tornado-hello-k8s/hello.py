import tornado.ioloop
import tornado.web
import socket
import logging

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
log = logging.getLogger(__name__)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        log.info(msg)
        self.write(msg)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(9001)
    fh = open('version.txt')
    ver = fh.read()
    fh.close()
    msg = "Hello, world | from host %s(%s) | %s" % (hostname, ip_address, ver)
    tornado.ioloop.IOLoop.current().start()
