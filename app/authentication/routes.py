from forms import UserSignupForm, UserLoginForm, UserProfileForm
from models import User, Profile, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

# imports for flask login 
from flask_login import login_user, logout_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            first = form.first.data
            last = form.last.data
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(first=first, last=last, email=email, password = password)

            db.session.add(user)
            db.session.commit()


            flash(f'You have successfully created a user account {email}', 'User-created')
            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('sign_up.html', form=form)





@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successful in your initiation. Congratulations, Entrant. Welcome to the Jedi Knights', 'auth-sucess')
                print("if")
                return redirect(url_for('site.profile'))
            else:
                print("else")
                flash('You have failed in your attempt to access this content. Must be 99 or older to enter this website', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        print("except")
        raise Exception('Invalid Form Data: Please Check your Form')
    return render_template('sign_in.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.home'))

@auth.route('/addprofile', methods = ['GET', 'POST'])
def addprofile():
    form = UserProfileForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            display_name = form.display_name
            profession = form.profession
            phone_number = form.phone_number
            location = form.location
            hobbies = form.hobbies

            profile = Profile(display_name=display_name, profession=profession, phone_number=phone_number, location=location, hobbies=hobbies)

            db.session.add(profile)
            db.session.commit()


            flash(f'You have successfully changed your profile.')
            return redirect(url_for('site.profile'))
    except:
        raise Exception('Invalid form data')
    
    return render_template('addprofile.html', form=form)