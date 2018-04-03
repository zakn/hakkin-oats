import http.server
import socketserver


def run(server_class=http.server.HTTPServer, handler_class=http.server.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()



class reqHandler(http.server.BaseHTTPRequestHandler):

    #GET
    def do_GET(self):
        #status code
        self.send_response(200)

        #headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        #message
        m = 'hello intranet!'

        #write message
        self.wfile.write(bytes(m, 'utf-8'))

def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('', 8081)
  httpd = http.server.HTTPServer(server_address, reqHandler)
  print('running server...')
  httpd.serve_forever()


run()

