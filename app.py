from flask import Flask, render_template, request, flash
from pip import main
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
from config import mail_username, mail_password

app = Flask(__name__)



app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSl'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password


mail = Mail(app)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')

@app.route('/Meals')
def Meals():
    return render_template('Meals.html')


@app.route('/Services')
def Services():
    return render_template('Services.html')


@app.route('/Gallery')
def Gallery():
    return render_template('Gallery.html')

@app.route('/FAQs')
def FAQs():
    return render_template('FAQ.html')


@app.route("/ContactUs", methods = ['GET' , 'POST'])
def contactForm():
    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email')
        phone = request.form.get('Phone')
        message = request.form.get('Message')

        msg = Message(subject=f"Mail from{name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender="fffffffffffffffffff1906@outlook.com", recipients=['teffinoexpress@gmail.com'])
        mail.send(msg)
        return render_template("ContactUs.html", success=True)

    return render_template('ContactUs.html')

        # Whatsapp_link = "https://wa.me/+918770053222?"


if __name__ == '__main__':
    app.run()
