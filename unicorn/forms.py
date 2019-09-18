# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError


class ConfigureWifiForm(Form):
    ssid = StringField('Access Point', validators=[
        InputRequired(),
        Length(min=1, max=32)
    ])
    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=8, max=64)
    ])
    security_mode = SelectField(
        'Security mode',
        choices=[
            ('WEP', 'WEP'),
            ('WPA_WPA2P', 'WPA/WPA2 Personal'),
            ('WPA2P', 'WPA2 Personal')
        ],
    )

    @staticmethod
    def validate_ssid(self, ssid):
        """
        The SSID can consist of up to 32 alphanumeric, case-sensitive,
        characters. The first character cannot be the !, #, or ; character.
        The +, ], /, ", TAB, and trailing spaces are invalid characters
        for SSIDs.

        However, I know for a fact that the "/" is accepted in SSIDs!
        """
        bad_chars = '+]"\t'
        bad_first_chars = '!#;'

        if ssid.data[0] in bad_first_chars:
            raise ValidationError(
                "The SSID should not contain '{}' as the "
                "first symbol.".format(ssid.data[0]))

        illegal_chars = set(ssid.data) & set(bad_chars)
        if len(illegal_chars) == 1:
            raise ValidationError(
                "The SSID should not contain the "
                "'{}' symbol.".format(illegal_chars[0]))
        elif len(illegal_chars) > 1:
            illegal_chars_for_display = ", ".join(illegal_chars)
            raise ValidationError(
                "The SSID should not contain any of these "
                "symbols: {}.".format(illegal_chars_for_display))
