from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5
import os

# Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('D61_secret_key')
bootstrap = Bootstrap5(app)


# Flask form
class NameForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])  # or label = "E-mail", same with password
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    login = SubmitField('Submit')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    email = None
    password = None
    form = NameForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == 'admin@email.com' and password == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html',
                           email=email,
                           password=password,
                           form=form, )


if __name__ == '__main__':
    app.run(debug=True)
