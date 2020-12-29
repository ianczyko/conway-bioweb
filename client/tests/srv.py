## @file client/tests/srv.py
#  @brief echo server for client unit testing

import os

try:
    # For Python 3.0 and later
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer



class MainHandler(BaseHTTPRequestHandler):
    """custom request handler"""

    def do_GET(self):
        """answer on http GET"""
        self.send_response(200)
        path = str(self.path)
        if 'connEcho' in path:
            self.send_header("Content-type", "text/html; charset=utf-8")
            query_components = parse_qs(urlparse(self.path).query)
            self.end_headers()
            self.wfile.write(query_components['callback'][0] + '("ala")')
        else:
            self.send_header("Content-type", "application/json;")
            self.end_headers()
            #self.wfile.write("<html><body>HELLO %s</body></html>" % str(self.path) )
            self.wfile.write("{\"ala\":\"ala\"}".encode('utf-8'))
        if path == '/exitApp':
            os._exit(0)


server_address = ('127.0.0.1', 50008)
httpd = HTTPServer(server_address, MainHandler)

sa = httpd.socket.getsockname()
httpd.serve_forever()
