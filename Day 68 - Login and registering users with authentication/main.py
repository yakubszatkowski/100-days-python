from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import NotFound
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This e-mail already exist.')
        else:
            hashed_password = generate_password_hash(
                password,
                method='pbkdf2:sha256',
                salt_length=8)
            new_user = User(email=email, password=hashed_password, name=name)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Invalid credentials. Please try again with different one.')
        else:
            flash('This email doesn\'t exist in our database')

        # # Other method which I honestly think is cool
        # try:
        #     user = db.one_or_404(db.select(User).filter_by(email=email))
        # except NotFound:
        #     flash('This email doesn\'t exist in our database')
        # else:
        #     if check_password_hash(user.password, password):
        #         login_user(user)
        #         return redirect(url_for('secrets'))
        #     else:
        #         flash('Invalid credentials. Please try again with different one.')

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    flash('You\'ve been logged out.')
    return redirect(url_for('login'))


@app.route('/download')
@login_required
def download():
    cheat_sheet_directory = r'.\static\files\cheat_sheet.pdf'
    return send_file(cheat_sheet_directory, as_attachment=False)  # if as_attachment is True then it downloads the file


if __name__ == "__main__":
    app.run(debug=True)
