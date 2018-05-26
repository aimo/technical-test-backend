# Run with "python client.py"
from bottle import get, run, static_file

@get('/')
def index():
    return static_file('index.html', root=".")

run(host='localhost', port=5000)
