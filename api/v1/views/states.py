#!/usr/bin/python3
""" Task for state"""
from api.v1.views.index import app_views, State
from models import storage
from flask import jsonify, request, abort, make_response

@app_views.route('/states', methods=['GET',
'POST'], strict_slaches=False)
def viewallthestatethings():
    """ fetch all the state objects"""
    if request.method == 'GET':
        stl=storage.all(State)
        states = [state.to_dict() for state in stl.values]
        return jsonify(states)
    if request.method == 'POST':
        try:
            body = request.get_json()
            if "name" not in Body.keys(): 
                return "Missing name", 400
            else:
                newstate = State(**body)
                newstate.save
                return jsonify(newstate.to_dict()), 201
        except:
            return "Not a JSON" , 400

@app_views.route('/states/<state_id>', 
strict_slashes = False, method = ['GET','DELETE','PUT'])
def stateidtime(state_id):
    stl =storage.get(State,state_id)
    if stl is not None:
        sd = stl.to_dict()
        if request.method == 'GET':
            return jsonify(sd)
        if request.method == 'DELETE':
            storage.delete(stl)
            storage.save()
            return jsonify({})
        
        if request.method == 'PUT':
            try:
                body= request.get_json()
                body.pop("id", "")
                body.pop("created_at", "")
                body.pop("updated_at", "")
                for k in body.keys():
                    setattr(stl, k, body.get(k))
                    stl.save()
                    sd = stl.to_dict()
                    return jsonify(sd)
            except:
                return "Not a JSON", 400
    else:
        abort(404)
