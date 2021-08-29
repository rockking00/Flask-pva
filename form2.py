# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired
from wtforms.fields import core


csrf = CSRFProtect()


class PayForm(FlaskForm):
    amount = StringField('Amount', validators=[DataRequired('Amount is required')])


    accounts = core.SelectField(
        label='Accounts',
        choices=(
            ('0.1','facebook - $1.2'),
            ('0.2','tweite - $1.5'),
            ('0.3','instagram - $1.6'),
        )
    )

    # payment = core.SelectField(
    #     label='支付方式',
    #     choices=(
    #         ('Perfectmoney', 'Perfectmoney'),
    #         ('payssion', 'payssion')
    #     )
    # )
    submit2 = SubmitField('OK')
