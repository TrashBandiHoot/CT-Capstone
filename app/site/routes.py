from flask import Blueprint, render_template
import urllib.request, json

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    url = "https://api.quotable.io/random?maxLength=300"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    quote = dict['content']
    author = dict['author']

    return render_template('profile.html', quote=quote, author=author)
