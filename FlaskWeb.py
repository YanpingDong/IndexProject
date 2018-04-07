#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from flask import Flask, redirect, url_for, request, render_template
from flask_login import LoginManager, current_user, login_user, login_required, UserMixin,logout_user

app = Flask(__name__)
app.secret_key = '123'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # 定义登录的 视图
login_manager.login_message = '请登录以访问此页面'  # 定义需要登录访问页面的提示消息

users = {'foo@bar.tld': {'password': 'secret'}}

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

class User(UserMixin):
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/n')
def indexn():
    return render_template('n.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form['email']
    print(email)
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

@app.route('/logout')
def logout():
    logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return '''
                   <form action='../login' method='POST'>
                    <input type='text' name='email' id='email' placeholder='email'/>
                    <input type='password' name='password' id='password' placeholder='password'/>
                    <input type='submit' name='submit'/>
                   </form>
                   '''

if __name__ == '__main__':
    app.run(debug=True,port=8000)