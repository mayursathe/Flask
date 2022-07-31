from click import password_option
from flask import redirect, url_for, request, render_template
from app import app, db
from db import User
from models import login_check

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

@app.route('/login',methods = ['POST', 'GET'])
def login():
   form = login_check()
   error = None
   if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user == None:
         error = 'Invalid Username or Password.'
      elif form.password.data == user.password:
         return redirect(url_for('success',name = user.username))
      else:
         error = 'Invalid Username or Password.'

   return render_template("check_user_data.html",form=form,error=error)



if __name__ == '__main__':
   app.run(debug = True)