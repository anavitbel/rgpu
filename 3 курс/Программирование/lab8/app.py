import mimetypes
from jinja2 import Environment, PackageLoader, select_autoescape
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote

env = Environment(
    loader=PackageLoader('app', 'templates', 'utf-8'),
    autoescape=select_autoescape(['html', 'xml']))


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        from pathlib import Path
        if self.path.count('png') == 1:
            imgname = self.path
            imgname = Path(imgname[1:])
            if not(imgname.exists()):
                self.create_image(imgname)
            self.send_image(imgname)

        elif self.path.count('ico') == 1:
            return
        elif self.path.count('users') == 1:
            self.user_page()
        else:
            self.index_page()

    def index_page(self):
        import models
        import views.client as client_view
        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()
        cinit = models.client.Client(None, None, None, None)
        c = models.client.Client.reading_data(cinit)
        from pathlib import Path
        my_file = Path("example2.csv")
        if not (my_file.exists()):
            result = client_view.render_client("Индексная страница", None, 'styles.html', 'form.html', None, None)
        else:
            result = client_view.render_client("Индексная страница", c, 'styles.html', 'form.html', 'table.html', None)
        result = bytes(result, 'utf-8')
        self.wfile.write(result)

    def user_page(self):
        import models
        import views.client as client_view
        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()
        body = self.path.split('/')[-1]
        cinit = models.client.Client(None, None, None, None)
        c = models.client.Client.reading_data(cinit, body=body)
        body = body + ".png"
        result = client_view.render_client("Индексная страница", c, 'styles.html', None, 'table.html', body)
        result = bytes(result, 'utf-8')
        self.wfile.write(result)

    def send_image(self, imgname):
        mimetype = mimetypes.MimeTypes().guess_type(imgname)[0]
        self.send_response(200)

        self.send_header('Content-type', mimetype)
        self.end_headers()
        imgfile = open(imgname, 'rb').read()
        self.wfile.write(imgfile)
        return

    def create_image(self, imgname):
        import qrcode
        img = qrcode.make("http://localhost:8000/" + str(imgname).replace("\\", "/")[:-4])
        img.save(str(imgname))

    def do_POST(self):

        import models

        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body = str(body, 'utf-8')
        body = unquote(body)
        print(body)

        cinit = models.client.Client(None, None, None, None)
        c = models.client.Client.writing_data(cinit, body)
        if c:
            result = f'<html><head><title>OK. Data got.</title><meta charset="utf-8"></head><body><h1>Данные получены!</h1><p><a href="http://localhost:8000/">Назад</a></p></body></html>'
        else:
            result = f'<html><head><title>ОШИБКА.</title><meta charset="utf-8"></head><body><h1>Такой email уже есть! Или база данных переполнена</h1><p><a href="http://localhost:8000/">Назад</a></p></body></html>'

        result = bytes(result, 'utf-8')

        self.wfile.write(result)


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
