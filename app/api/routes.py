from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from helpers import token_required
from models import db, Profile, profile_schema, profile_schemas, UserBooks
from forms import UserProfileForm
from flask_login import current_user
import json

api = Blueprint('api',__name__, url_prefix='/api')



@api.route('/addprofile', methods = ['GET', 'POST'])
def add_profile():
    form = UserProfileForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            display_name = form.display_name.data
            profession = form.profession.data
            phone_number = form.phone_number.data
            location = form.location.data
            hobbies = form.hobbies.data
            user_token = current_user.token
            print(phone_number, location)

            profile = Profile(display_name=display_name, profession=profession, phone_number=phone_number, location=location, hobbies=hobbies, user_token=user_token)

            db.session.add(profile)
            db.session.commit()

            
            flash(f'You have successfully added your profile')
            return redirect(url_for('site.profile'))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('addprofile.html', form=form)


@api.route('/profile/get/<token>', methods = ['GET'])
def get_profile(token):
    print(token, 'here')
    profile = Profile.query.filter_by(user_token = token).first().__dict__
    print(profile)
    profile_id = profile['id']
    profile_details = Profile.query.filter_by(id = profile_id).first()
    response = profile_schema.dump(profile_details)
    return jsonify(response)
    

# Updating
@api.route('/profile/update', methods = ['GET', 'POST', 'PUT'])
def update_profile():
    form = UserProfileForm()
    try:
        if form.validate_on_submit():
            user_profile = Profile.query.filter_by(user_token = current_user.token).first().__dict__
            profile_id = user_profile['id']
            profile = Profile.query.filter_by(id = profile_id).first()
            profile.display_name = form.display_name.data
            profile.profession = form.profession.data
            profile.phone_number = form.phone_number.data
            profile.location = form.location.data
            profile.hobbies = form.hobbies.data

            db.session.commit()
            

            
            flash(f'You have successfully updated your profile')
            return render_template('profile.html')
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('updateprofile.html', form=form)



# id is book ID user_token will be hard coded
@api.route('/addbook/<id>', methods = ['POST'])
def addbook(id):
    token = '6cb18f60ae70938f564f3552c8b6bf33919db50c97a0f8c0'

    book = UserBooks(book_id=id, user_token=token)

    db.session.add(book)
    db.session.commit()
    return render_template('externalapi.html')

@api.route('/deletebook/<id>', methods=['DELETE'])
def deletebook(id):
    book = UserBooks.query.get(id)
    db.session.delete(book)
    db.session.commit()
    






