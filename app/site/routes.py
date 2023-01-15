from flask import Flask, request, Blueprint, render_template
import urllib.request, json
import psycopg2
from forms import UserProfileForm
from flask_login import current_user
from models import db, User, Profile, profile_schema, UserBooks


site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/eapi')
def eapi():
    books = UserBooks.query.all()
    return render_template('externalapi.html', books = books)

# Pull data from local api and third party api to display on profile page

@site.route('/profile')
def profile():
    url = "https://api.quotable.io/random?maxLength=300"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    quote = dict['content']
    author = dict['author']

    user_token = current_user.token
    print(user_token)

    base_url = 'https://coding-temple-capstone.herokuapp.com/api/profile/get/'
    prof_url = base_url + user_token
    print(prof_url)

    prof_response = urllib.request.urlopen(prof_url)
    prof_data = prof_response.read()
    prof_dict = json.loads(prof_data)
    display_name = prof_dict['display_name']
    profession = prof_dict['profession']
    phone_number = prof_dict['phone_number']
    location = prof_dict['location']
    hobbies = prof_dict['hobbies']

    return render_template('profile.html', quote=quote, author=author, display_name=display_name, profession=profession, phone_number=phone_number, location=location, hobbies=hobbies)


# @site.route('/profile/update', methods = ['GET', 'POST'])
# def updateprofile():
#     form = UserProfileForm()
#     return render_template('updateprofile.html', form=form)