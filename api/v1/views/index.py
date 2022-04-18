#!/usr/bin/python3
""" index route"""

import json
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models import city
from models.amenity import Amenity
from models.city import City
from models.state import State
from models .place import Place
from models.review import Review
from models.user import User

@app_views.route('/status')
def status():
    """ display status"""
    return jsonify({ 'status':"OK"})

@app_views.route('/stats')
def stats():
    """ get the count of each object in storage"""
    new_dict = {}
    new_dict['amenities'] =  storage.count(Amenity)
    new_dict['city'] = storage.count(City)
    new_dict['states'] = storage.count(State)
    new_dict['place'] = storage.count(Place)
    new_dict['review'] = storage.count(Review)
    new_dict['userss'] = storage.count(User)
    return jsonify(new_dict)
