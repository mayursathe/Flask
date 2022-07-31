from click import password_option
from flask import redirect, url_for, request, render_template, flash
from app import app, db
from db import User
from models import login_check

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.db"


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
   if form.validate_on_submit():
      try:
         user = User.query.filter_by(username=form.username.data).first()
         if form.password.data == user.password:
            return redirect(url_for('success',name = user.username))
         else:
            flash('Invalid Username or Password.', 'danger')
      except Exception as e:
         flash(e,'danger')
   return render_template("check_user_data.html",form=form)



if __name__ == '__main__':
   app.run(debug = True)