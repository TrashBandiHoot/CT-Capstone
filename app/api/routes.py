from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from helpers import token_required
from models import db, Profile, profile_schema, profile_schemas
from forms import UserProfileForm
import urllib.request, json
import os

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'foo' : 'bar'}


@api.route('/profile', methods = ['GET', 'POST'])
def add_profile():
    form = UserProfileForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            display_name = form.display_name.data
            profession = form.profession.data
            phone_number = form.phone_number.data
            location = form.location.data
            hobbies = form.hobbies.data
            print(phone_number, location)

            profile = Profile(display_name=display_name, profession=profession, phone_number=phone_number, location = location, hobbies = hobbies)

            db.session.add(profile)
            db.session.commit()


            flash(f'You have successfully created a user account {phone_number}', 'User-created')
            return redirect(url_for('profile.home'))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('addprofile.html', form=form)

# Updating
@api.route('/profile/<id>', methods = ['POST', 'PUT'])
def update_profile(current_user_token, id):
    profile = Profile.query.get(id)
    profile.display_name = request.json['display_name']
    profile.profession = request.json['profession']
    profile.phone_number = request.json['phone_number']
    profile.location = request.json['location']
    profile.hobbies = request.json['hobbies']
    profile.user_token = current_user_token.token

    db.session.commit()
    response = profile_schema.dump(profile)
    return jsonify(response)

# Delete
@api.route('/profile/<id>', methods = ['DELETE'])
@token_required
def delete_contact(current_user_token, id):
    profile = Profile.query.get(id)
    db.session.delete(profile)
    db.session.commit()
    response = profile_schema.dump(profile)
    return jsonify(response)








# @api.route('/coffees', methods = ['POST'])
# @token_required
# def create_coffee(current_user_token):
#     name = request.json['name']
#     cream = request.json['cream']
#     added_flavor = request.json['added_flavor']
#     user_token = current_user_token.token

#     profile = Coffee(name, cream, added_flavor, user_token = user_token)

#     db.session.add(profile)
#     db.session.commit()

#     response = coffee_schema.dump(profile)
#     return jsonify(response)

# @api.route('/coffees', methods = ['GET'])
# @token_required
# def get_coffees(current_user_token):
#     a_user = current_user_token.token
#     coffees = Coffee.query.filter_by(user_token = a_user).all()
#     response = coffees_schema.dump(coffees)
#     return jsonify(response)

# @api.route('/coffees/<id>', methods = ['GET'])
# @token_required
# def get_single_coffee(current_user_token, id):
#     profile = Coffee.query.get(id)
#     response = coffee_schema.dump(profile)
#     return jsonify(response)



# # Updating
# @api.route('/coffees/<id>', methods = ['POST', 'PUT'])
# @token_required
# def update_car(current_user_token, id):
#     profile = Coffee.query.get(id)
#     profile.name = request.json['name']
#     profile.cream = request.json['cream']
#     profile.added_flavor = request.json['added_flavor']
#     profile.user_token = current_user_token.token

#     db.session.commit()
#     response = coffee_schema.dump(profile)
#     return jsonify(response)

# # Delete
# @api.route('/coffees/<id>', methods = ['DELETE'])
# @token_required
# def delete_contact(current_user_token, id):
#     profile = Coffee.query.get(id)
#     db.session.delete(profile)
#     db.session.commit()
#     response = coffee_schema.dump(profile)
#     return jsonify(response)