from click import password_option
from flask import Flask, redirect, url_for, request, render_template
from db import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.db"


@app.route('/')
def index():
   return render_template('login.html')

@app.route('/forgot_password')
def forgot_password():
   return render_template('forgot_password.html')

@app.route('/success/<name>')
def success(name):
   return render_template('success.html',name = name)
   #return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['login']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('login')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)