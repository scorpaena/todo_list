from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError


class PasswordComplexityValidator:
    def __call__(self, attrs):
        password1 = attrs["password1"]
        password2 = attrs["password2"]
        try:
            validate_password(password1)
        except DjangoValidationError as error:
            raise ValidationError(error)


class PasswordConfirmationValidator:
    def __call__(self, attrs):
        password1 = attrs["password1"]
        password2 = attrs["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError("password mismatch")
