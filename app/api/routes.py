from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Coffee, coffee_schema, coffees_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'foo' : 'bar'}

@api.route('/coffees', methods = ['POST'])
@token_required
def create_coffee(current_user_token):
    name = request.json['name']
    cream = request.json['cream']
    added_flavor = request.json['added_flavor']
    user_token = current_user_token.token

    coffee = Coffee(name, cream, added_flavor, user_token = user_token)

    db.session.add(coffee)
    db.session.commit()

    response = coffee_schema.dump(coffee)
    return jsonify(response)

@api.route('/coffees', methods = ['GET'])
@token_required
def get_coffees(current_user_token):
    a_user = current_user_token.token
    coffees = Coffee.query.filter_by(user_token = a_user).all()
    response = coffees_schema.dump(coffees)
    return jsonify(response)

@api.route('/coffees/<id>', methods = ['GET'])
@token_required
def get_single_coffee(current_user_token, id):
    coffee = Coffee.query.get(id)
    response = coffee_schema.dump(coffee)
    return jsonify(response)



# Updating
@api.route('/coffees/<id>', methods = ['POST', 'PUT'])
@token_required
def update_car(current_user_token, id):
    coffee = Coffee.query.get(id)
    coffee.name = request.json['name']
    coffee.cream = request.json['cream']
    coffee.added_flavor = request.json['added_flavor']
    coffee.user_token = current_user_token.token

    db.session.commit()
    response = coffee_schema.dump(coffee)
    return jsonify(response)

# Delete
@api.route('/coffees/<id>', methods = ['DELETE'])
@token_required
def delete_contact(current_user_token, id):
    coffee = Coffee.query.get(id)
    db.session.delete(coffee)
    db.session.commit()
    response = coffee_schema.dump(coffee)
    return jsonify(response)