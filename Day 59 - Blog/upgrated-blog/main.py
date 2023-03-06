from flask import Flask, render_template, request
import requests
import smtplib
import os

response = requests.get(url='https://api.npoint.io/81bab482e62ce81face5')
posts = response.json()

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        msg = f'Name: {name} \nE-mail: {email} \nPhone: {phone} \nMessage: {message}'
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user='rtyrtyqweqwe39@gmail.com', password=os.environ.get('D32_gmail_app_pass'))
            connection.sendmail(
                from_addr='rtyrtyqweqwe39@gmail.com', to_addrs='yakub.szatkowski@gmail.com',
                msg=f'Subject: New message from the blog! \n\n {msg}')
        return render_template('contact.html', post=True)
    else:
        return render_template('contact.html')


# @app.route('/form-entry', methods=["POST"])
# def receive_data():


@app.route(f'/<int:post_id>.html')
def post(post_id):
    post_id -= 1
    return render_template('post.html', post=posts[post_id])


if __name__ == '__main__':
    app.run(debug=True)
