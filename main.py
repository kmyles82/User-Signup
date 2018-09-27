from flask import Flask, request, render_template, redirect
import cgi
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<style>
    .error{{ color:red; }}
</style>
<form method="POST">
    <h1>User Signup</h1>
    <label for="name">Username
        <input type="text" name="name" id="name" value="{username}">
    </label>
    <p class="error">{username_error}</p>
    <label for="pwd">Password
        <input type="password" name="pwd" id="pwd" value="{pwd}">
    </label>
    <p class="error">{password_error}</p>
    <label for="confirm_pwd">Confirm Password
    <input type="password" name="confirm" id="confirm" value="{confirm}">
    </label>
    <p class="error">{confirm_error}</p>
    <label for="email">Email (optional)
        <input type="email" name="email" id="email" value="{email}">
    </label>
    <p class="error">{email_error}</p>
    <input type="submit" value="Submit">
</form>
"""

@app.route('/')
def display_form():
    
    return form.format(username='',pwd='',confirm='',email='',username_error='',password_error='',confirm_error='',email_error='')



@app.route('/', methods=['POST'])
def validate_input():

    username = request.form['name']
    password = request.form['pwd']
    confirm = request.form['confirm']
    email = request.form['email']
    match=re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)",email)
    username_error = ''
    password_error = ''
    confirm_error=''
    email_error = ''

    if username == '':
        username_error = 'Username cannot be empty'
    elif len(username) > 20 or len(username) < 3:
        username_error = 'Username must be between 3 - 20 characters'
        # username = ''
    elif ' ' in username:
        username_error = 'Spaces are not allowed in username'
        username = ''
    
    if password == '':
        password_error = 'Password cannot be empty'
    elif len(password) > 20 or len(password) < 3:
        password_error = 'Password must be between 3 - 20 characters'
        # password = ''
    elif ' ' in password:
        password_error = 'Spaces are not allowed in password'
        # password = ''
    
    if confirm == '':
        confirm_error = 'Confirm password cannot be empty'
    elif not confirm == password:
        confirm_error = 'Passwords does not match'
        # confirm = ''

    if email == '':
        email_error = ''
    elif not match or (len(email) < 3) or (len(email) > 20):
        email_error = 'Email address is invalid'
        # email = ''

    if not username_error and not password_error and not confirm_error and not email_error:
        return 'Welcome ' + username + '!'
        
    else:
        return form.format(username_error=username_error,password_error=password_error,confirm_error=confirm_error,email_error=email_error,username=username,email=email,pwd=password,confirm=confirm)


app.run()