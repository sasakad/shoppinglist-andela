from flask import Flask, render_template, flash, redirect, request, url_for,session, logging 
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt



app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

#create class called register passing Form as a paremeter
class RegisterForm(Form):
    name = StringField('Name',[validators.Length(min=1, max=50)])
    username = StringField('Username',[validators.Length(min=4, max=25)])
    email = StringField('Email',[validators.Length(min=6, max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Paasword do not much')
    ])
    confirm=PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        
       
       

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


    #this get,post are requests by get agtheres info allowing the page to load while the form post submits form to the registerpage
# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        
    return render_template('login.html')



# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))    


   #Dashboard
@app.route('/dashboard')
def dashboard():                                       
    return render_template('dashboard.html')

if __name__ == '__main__':
    #this allows us to run the pplication and it is developer mode thuenabling us not to restsrt the server everytime we make changes.
    app.run(debug=True)
