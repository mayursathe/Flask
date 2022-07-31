from click import password_option
from flask import redirect, url_for, request, render_template, make_response
from app import app, db, bcrypt, login_manager, COOKIE_TIME_OUT
from db import User
from models import login_check
from flask_bcrypt import check_password_hash

@app.route('/')
def index():
   form = login_check()
   return render_template('login.html',form=form)

@app.route('/forgot_password')
def forgot_password():
   return render_template('forgot_password.html')

@app.route('/success/<name>')
def success(name):
   return render_template('success.html',name = name)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   form = login_check()
   error = None
   if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user == None:
         error = 'Invalid Username or Password.'
      elif check_password_hash(user.password, form.password.data):
         remember_me = request.form.getlist('remember_me')
         if remember_me:
            remember_response = make_response(redirect(url_for('success',name = user.username)))
            remember_response.set_cookie('username', user.username, max_age=COOKIE_TIME_OUT)
            remember_response.set_cookie('email', user.email, max_age=COOKIE_TIME_OUT)
            remember_response.set_cookie('password', form.password.data, max_age=COOKIE_TIME_OUT)
            remember_response.set_cookie('remember_me', 'checked', max_age=COOKIE_TIME_OUT)
            return remember_response
         else:
            remember_response = make_response(redirect(url_for('success',name = user.username)))
            remember_response.set_cookie('username', '', expires=0)
            remember_response.set_cookie('email', '', expires=0)
            remember_response.set_cookie('password', '', expires=0)
            remember_response.set_cookie('remember_me', '', expires=0)
            return remember_response
      else:
         error = 'Invalid Username or Password.'

   return render_template("check_user_data.html",form=form,error=error)

if __name__ == '__main__':
   app.run(debug = True)