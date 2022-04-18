from importlib import resources
from logging import exception
import resource
from flask import Flask, make_response, jsonify
from models import storage
import os
from api.v1.views import app_views
from flask_cors import CORS

app= Flask(__name__)
app.regester_blueprint(app_views)
CORS(app,resources={r"*/":{"origins":"0.0.0.0"}})

@app.teardown_appcontext
def close(exception):
    """ this function will close a session and reload"""
    storage.close

@app.errorhandler(404)
def error(error):
    """ this fuction will jsonfy when there is an error"""
    return make_response(jsonify({"error":"Not found"}),404)

if __name__ == "__main__":
    app.run(host = os.getenv('HBNB_API_HOST'), port = os.getenv('HBNB_API_PORT'),
            threaded = True)
