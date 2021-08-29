# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, Email


csrf = CSRFProtect()

class ContactForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('Email is required'),Email('Enter a valid email')])
    message = TextAreaField('Message', validators=[DataRequired('Message cannot be empty')])
    submit = SubmitField("Submit")
