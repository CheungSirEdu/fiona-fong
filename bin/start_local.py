#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os
import webbrowser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PORT = 8777


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))


httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
url = "http://127.0.0.1:%s/" % PORT
print("本機網站：", url)
webbrowser.open(url)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
