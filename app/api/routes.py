from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from helpers import token_required, get_token
from models import db, Profile, User, profile_schema, profile_schemas
from forms import UserProfileForm


api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'foo' : 'bar'}


@api.route('/addprofile', methods = ['GET', 'POST'])
def add_profile(current_user_token = get_token):
    form = UserProfileForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            display_name = form.display_name.data
            profession = form.profession.data
            phone_number = form.phone_number.data
            location = form.location.data
            hobbies = form.hobbies.data
            user_token = current_user_token
            print(phone_number, location)

            profile = Profile(display_name=display_name, profession=profession, phone_number=phone_number, location = location, hobbies = hobbies, user_token = user_token)

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
def delete_profile(current_user_token, id):
    profile = Profile.query.get(id)
    db.session.delete(profile)
    db.session.commit()
    response = profile_schema.dump(profile)
    return jsonify(response)








