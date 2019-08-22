import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=5001, type=int, help="port to listen on")
    args = parser.parse_args()

    os.chdir('static')
    server_address = ('', args.port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('serving at http://192.168.2.106:%d' % args.port)
    httpd.serve_forever()
main()
