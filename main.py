from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    '''Display home page'''
    return render_template('hello.html', title="User Sign-in App")

def is_valid_username_pw(password):
    '''Validate string and return True if it is between 3 and 20 characters long'''

    if len(password) >= 3 and len(password) <= 20:
        if not re.search(r'\s', password):
            return True
    else:
        return False

@app.route('/', methods=['POST'])
def validate_user():
    '''Validate username, password and email address entered. If invalid return an error'''

    name = request.form['name']
    password = request.form['password']
    password_check = request.form['password_check']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_check_error = ''
    email_error = ''

    if not is_valid_username_pw(name):
        username_error = 'Not a valid username'

    if not is_valid_username_pw(password):
        password_error = 'Not a valid password'
        password = ''
    else:
        if password_check != password:
            password_check_error = 'Your passwords did not match'
            password = ''
            password_check = ''

    if email:
        if not re.match("([^@|\s]+@[^@]+\.[^@|\s]+)", email):
            email_error = 'Not a valid email'

    if not password_check_error and not password_error and not email_error and not username_error:
        return render_template('welcome.html', title="Welcome User", name=name)
    else:
        return render_template('hello.html', password_error=password_error,
                               username_error=username_error,
                               password_check_error=password_check_error,
                               email_error=email_error, name=name, email=email,
                               title='Sign-in Page')



app.run()


