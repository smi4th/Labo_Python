from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from flask_bcrypt import Bcrypt

from forms import *
from Models import *

#pip install flask_bcrypt; flask_wtf; flask_login; flask_SQLAlchemy==2.5.1; flask

#To create the database:
#1. create environment : python3 -m venv tutorial-env
#2. activate environment : tutorial-env\Scripts\activate.bat
#3. open a git bash console in the folder where the app.py file is located
#4. run the command : sqlite3 <name>.db
#5. run the command : .tables
#6. run the command : .exit
#Do the 4-6 steps for each database you want to create
#7. run the command : python3
#8. run the command : from app import db
#9. run the command : db.create_all()
#10. run the command : exit()

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_BINDS'] = {
    'forum': 'sqlite:///forum.db',
    'messageInForum': 'sqlite:///messageInForum.db'
}
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

# ------------------- FORUM ------------------- #
@app.route('/forum', methods=['GET', 'POST'])
@login_required
def forum():
    form = CreateForumForm()
    if form.validate_on_submit():
        new_forum = Forum(title=form.title.data, description=form.description.data, author=current_user.username)
        db.session.add(new_forum)
        db.session.commit()
        return redirect(url_for('forum'))

    return render_template('forum.html', createForum=form, forums=Forum.query.all())

@app.route('/forum/<forum_id>', methods=['GET', 'POST'])
@login_required
def forumMessages(forum_id):
    
    form = CreateMessageInForumForm()
    if form.validate_on_submit():
        new_messageInForum = MessageInForum(message=form.message.data, author=current_user.username, forum_id=forum_id)
        db.session.add(new_messageInForum)
        db.session.commit()
        return redirect(url_for('forumMessages', forum_id=forum_id))

    return render_template('forumMessages.html', createMessageInForum=form, messages=MessageInForum.query.order_by(MessageInForum.date).filter_by(forum_id=forum_id).all(), forum=Forum.query.get(forum_id))
# -------------------       ------------------- #

# --------------------- USERS --------------------- #
@app.route('/users', methods=['GET', 'POST'])
def users():
    return render_template('users.html', users=User.query.all())

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    user = User.query.get(id)
    db.session.delete(user) #Object '...' is already attached to session '...' (this is '...') (Background on this error at: http://sqlalche.me/e/13/bhk3)
    db.session.commit()
    return redirect(url_for('users'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    db.session.pop("user_id", None)
    return redirect(url_for('login'))

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)
# ---------------------       --------------------- #

# --------------------- START --------------------- #
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
# ---------------------       --------------------- #