import tornado.ioloop
import tornado.web
import time
import math


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class PrometheusHandler(tornado.web.RequestHandler):
    x = 0
    def get(self, *args, **kwargs):
        PrometheusHandler.x += 1
        self.render("prometheus.template", **dict(current_timestamp=int(time.time()),
                                                  number=PrometheusHandler.x,
                                                  sin_number=math.sin(PrometheusHandler.x)))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/prometheus", PrometheusHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(9000)

    tornado.ioloop.IOLoop.current().start()