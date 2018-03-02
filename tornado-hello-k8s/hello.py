import tornado.ioloop
import tornado.web
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world from host %s(%s)" % (hostname, ip_address))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(9000)
    tornado.ioloop.IOLoop.current().start()
