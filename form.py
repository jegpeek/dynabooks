import flask
from flask import Flask, request
 
# App config.
#form = Flask('formapp', static_url_path='')
DEBUG = True
app = Flask(__name__, static_url_path='')
 
@app.route("/")
def root():
    return app.send_static_file('index.html')
 
if __name__ == "__main__":
    app.debug = True
    app.run()
