from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def validate(self, password, user=None):
        # Check that password is decimal
        if not password.isdecimal():
            raise ValidationError(
                _("The password must contain only numeric digits, 0-9."),
                code='password_no_number',
            )
        try:
            val = int(password)
        except ValueError:
            raise ValidationError(
                _("The password must contain only numeric digits, 0-9."),
                code='password_no_number',
            )
        if not len(password) == 6:
            raise ValidationError(
                _("The password must contain 6 digits."),
                code='password_length',
            )

    def get_help_text(self):
        return _(
            "Your password must contain only  numeric digits, 0-9."
        )


class LengthValidator(object):

    def validate(self, password, user=None):
        if not len(password) == 6:
            raise ValidationError(
                _("The password must contain 6 digits."),
                code='password_length',
            )

    def get_help_text(self):
        return _(
            "Your password must contain 6 digits."
        )
