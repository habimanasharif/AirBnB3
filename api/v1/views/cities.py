#!/usr/bin/python3
""" city"""
from api.v1.views.index import app_views, State, City
from models import storage
from flask import jsonify, request, abort

@app_views.route('/states/<state_id>/cities',
strict_slashes=False,methods=['GET','POST'])
def citytime(state_id):
    """ handle a state object with said id depending on HTTP request"""
    stl=storage.all(State)
    k= "state." + state_id 
    if k in stl.keys():
        s= stl.get(k)
        sd=s.to_dict()
        if request.method == 'GET':
            cl = []
            for city in s.cities:
                cl.append(city.to_dict())
            return jsonify(cl)
        if request.method == 'POST':
            try:
                body = request.get_json()
                if "name" not in body.keys():
                    abort(400, "Missing name")
                else:
                    body.updtae({'state_id': state_id})
                    newcity = City(**body)
                    newcity.save()
                    return jsonify(newcity.to_dict()), 201
            except:
                abort(400, "Not a JSON")
    else:
        abort(404)
@app_views.route('/cities/<city_id>', 
strict_slashes = False, methods=['GET', 'DELETE', 'PUT'])
def truecityfun(city_id):
    """ HAndle a city objects with said Id"""
    ctl = storage.all(City)
    k="city." + city_id
    if k in ctl.keys():
        c= ctl.get(k)
        cd= c.to_dict()
        if request.method == 'GET':
            return jsonfy(cd)
        if request.method == 'DELETE':
            storage.delete(c)
            storage.save()
        if request.method == 'PUT':
            try:
                body = request.get_json()
                body.pop('id', '')
                body.pop('created_at', '')
                body.pop('updated_at', '')
                for k in body.keys():
                    setattr(c,k,body.get(k))
                    c.save()
                    cd = c.to_dict()
                    return jsonify(cd)
            except:
                abort(400,'Not a JSON')
    else:
        abort(404)
        