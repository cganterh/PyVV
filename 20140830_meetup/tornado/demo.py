from tornado.web import StaticFileHandler, RequestHandler, Application
from tornado.ioloop import IOLoop

class Handler(RequestHandler):
    mensajes = []
    
    def get(self):
        self.render('home.html', mensajes=self.mensajes)
    
    def post(self):
        mensaje = self.get_argument('mensaje')
        if mensaje:
            self.mensajes.append(mensaje)
        self.render('home.html', mensajes=self.mensajes)

handlers = [('/$', Handler),
            ('/(style.css)$', StaticFileHandler, {'path': '.'})]

app = Application(handlers, debug=True)

if __name__ == "__main__":
    app.listen(8888)
    IOLoop.instance().start()
