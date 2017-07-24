#/bin/python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import SimpleHTTPServer
import robot


robot = robot.Robot()

class RobotHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/javascript')
        self.end_headers()

    def do_GET(self):
        prefix = "/action/"
        # Serve files normally
        if (not self.path.startswith(prefix)):
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

        (action, dx, dy) = self.parse(self.path[len(prefix):])
        print "Action: " + action
        print "dx: %f / dy: %f" % (dx, dy)
        action_method = getattr(robot, action)
        action_method(dx, dy)

        # Handle action requests
        self._set_headers()
        self.wfile.write("{{'action': '{0}'}}".format(action))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

    def parse(self, pathPart):
        qmark = pathPart.find("?")

        action = pathPart[0:qmark]
        query = pathPart[qmark + 1:]
        params = dict(token.split('=') for token in query.split("&"))
        print params
        dx = float(params["dx"])
        dy = float(params["dy"])
        return (action, dx, dy)

def run(server_class=HTTPServer, handler_class=RobotHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()