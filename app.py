from flask import Flask
from dotenv import load_dotenv
import socket
import os

app = Flask(__name__)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
load_dotenv()

PORT = os.environ['PORT']

localIp = s.getsockname()[0]

@app.route('/', methods=['GET'])
def index():
  return '<h1>cuida</h1>'
  
app.run(port = PORT, host = localIp, debug = True)