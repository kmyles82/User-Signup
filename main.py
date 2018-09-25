from flask import Flask, request, render_template, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

# @app.route('/')
# def index():
#     return 'Hello'

@app.route('/signup',methods=['POST', 'GET'])
def signup():
    error = ''

    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        confirm_pwd = request.form.get('confirm_pwd')
        email = request.form.get('email')

        if (name == '') or (pwd == '') or (email == ''):
            error = 'Please fill out each field'
            return redirect('/?signup' + error)

        if (len(name) < 3 or len(name) > 20) or (pwd < 3 or pwd > 20):
            error = 'Username or password is invalid, must be between (3 - 20) characters'
            return redirect("/?signup" + error)
        
        if (' ' in name) or (' ' in pwd):
            error = 'Password or password is invalid, neither cannot contain a space character'
            return redirect("/?signup" + error)

        if (confirm_pwd == pwd):
            error = 'Passwords does not match'
            return redirect("/?signup" + error)

        if email == '':
            error = ''
        elif (email != '') and ("@" not in email) and ("." not in email) and (email < 3 and email > 20):
            error = "Email address is invalid"
            return redirect('/?signup' + error)

    return render_template('/signup.html',error=error)



app.run()