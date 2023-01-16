from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from helpers import token_required
from models import db, Profile, profile_schema, profile_schemas, UserBooks, BookSchema
from forms import UserProfileForm
from flask_login import current_user
import json, urllib.request

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
    base_url = 'https://www.googleapis.com/books/v1/volumes/'
    target_url = base_url + id

    response = urllib.request.urlopen(target_url)
    data = response.read()
    dict = json.loads(data)
    token = '1e267e224df941eba6bcacc7809a3ee550d021e9b6113cbe'
    title = dict['volumeInfo']['title']
    imgurl = dict['volumeInfo']['imageLinks']['smallThumbnail']
    book = UserBooks(book_id=id, title=title, imgurl=imgurl, user_token=token)

    db.session.add(book)
    db.session.commit()
    return redirect(url_for('site.eapi'))

@api.route('/deletebook/<id>', methods=['DELETE'])
def deletebook(id):
    id = str(id)
    book = UserBooks.query.filter_by(book_id = id).first()
    print(book)
    db.session.delete(book)
    db.session.commit()
    response = BookSchema.dump(book)
    return jsonify(response)

    






