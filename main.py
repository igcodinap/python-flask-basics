# importamos libreria http
import http.server

# cree una clase que extiende de http.server.BaseHTTPRequestHandler
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # la ruta
        if self.path == '/':
            # enviamos la respuesta
            # elcodigo de la respuesta
            self.send_response(200)
            # las cabeceras
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # el cuerpo de la respuesta
            self.wfile.write(b"Hello, world!")
        else:
            self.send_response(404)


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print("Serving on localhost:8000")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

## en ambos:
# importamos una libreria
# definimos rutas
# definimos metodos
# corrimos la app
