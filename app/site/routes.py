from flask import Flask, request, Blueprint, render_template
import urllib.request, json
import psycopg2
from forms import UserProfileForm


site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

# Pull data from local api and third party api to display on profile page

@site.route('/profile')
def profile():
    url = "https://api.quotable.io/random?maxLength=300"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    quote = dict['content']
    author = dict['author']

    prof_url = 'http://127.0.0.1:5000/api/profile/get'

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