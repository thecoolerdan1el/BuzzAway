# login.py
from flask import Blueprint, request, render_template, redirect, url_for
login_ = Blueprint("login_",__name__, template_folder="templates")

users = {
    'user1':'1234',
    'user2':'12345'
}
@login_.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':    
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('base.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('base.html')
    
@login_.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("user.html", devices=users)
    
@login_.route('/remove_user')
def remove_user():
    global users
    return render_template("remove_user.html", devices=users)

@login_.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template("user.html", devices=users)