# -*- coding: utf-8 -*-
from flask import render_template, Flask, request, redirect
from flask_mail import Message, Mail
from forms import csrf, ContactForm
from form2 import PayForm
from pymongo import MongoClient
import os


app = Flask(__name__)

app_ctx = app.app_context()
app_ctx.push()

SECRET_KEY = os.urandom(64)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)


app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)

client = MongoClient()
DB = client['PVA']
acc = DB['ACC']


@app.route('/', methods=['GET'])
def home():
    homeform = PayForm()
    return render_template('index.html', homeform=homeform)


@app.route('/index', methods=['GET', 'POST'])
def postaction():
    if request.method == 'POST':
        amount = request.form['amount']
        accounts = request.form['accounts']
        PAYMENT_AMOUNT = request.form['PAYMENT_AMOUNT']
        doc = {
            '数量': amount,
            '账号': accounts
        }
        acc.insert_one(doc)
        return render_template('newpage.html', amount=amount, accounts=accounts, payment=PAYMENT_AMOUNT)


@app.route('/contact', methods=['GET', 'POST'])
def mail_1():
    forms = ContactForm()
    if request.method == 'POST':
        seed_message(request.form)
    return render_template('mail.html', form=forms)


def seed_message(message):
    msg = Message(sender = 'sbz@sitebuilderzone.com', subject=message.get('email'),
                  recipients=['sbz@sitebuilderzone.com'],
                  body=message.get('message')
                  )
    mail.send(msg)



if __name__ == '__main__':
    app.run(debug=True)

