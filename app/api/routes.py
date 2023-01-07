from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from helpers import token_required
from models import db, Profile, User, profile_schema, profile_schemas
from forms import UserProfileForm


api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/getdata')
def getdata():
    return {'foo' : 'bar'}


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
            print(phone_number, location)

            profile = Profile(display_name=display_name, profession=profession, phone_number=phone_number, location = location, hobbies = hobbies)

            db.session.add(profile)
            db.session.commit()

            
            flash(f'You have successfully added your profile')
            return redirect(url_for('site.profile'))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('addprofile.html', form=form)


@api.route('/profile/get', methods = ['GET'])
def get_profile():
    profile_details = Profile.query.get('21JQeuJZSUXxgpCwlzVCkEDPg-59QAri_M2ekHTmq2Q')
    response = profile_schema.dump(profile_details)
    return jsonify(response)
    

# Updating
@api.route('/profile/update', methods = ['GET', 'PUT'])
def update_profile():
    form = UserProfileForm()
    try:
        if request.method == 'PUT' and form.validate_on_submit():
            profile = Profile.query.get('21JQeuJZSUXxgpCwlzVCkEDPg-59QAri_M2ekHTmq2Q')
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
    return redirect(url_for('profile.html'))

# Delete
@api.route('/profile/delete', methods = ['DELETE'])
@token_required
def delete_profile():
    profile = Profile.query.get('21JQeuJZSUXxgpCwlzVCkEDPg-59QAri_M2ekHTmq2Q')
    db.session.delete(profile)
    db.session.commit()
    response = profile_schema.dump(profile)
    return jsonify(response)








