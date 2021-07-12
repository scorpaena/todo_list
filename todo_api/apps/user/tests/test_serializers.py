import pytest
from apps.user.serializers import UserSignUpSerializer

def test_user_signup_serializer(db):
    serializer = UserSignUpSerializer(
        data = {
            "username": "foo",
            "password1": "bar123$%",
            "password2": "bar123$%",
        }
    )
    assert serializer.is_valid()

def test_user_serializer_pass_complexity_validator(db):
    serializer = UserSignUpSerializer(
        data = {
            "username": "foo",
            "password1": "bar123",
            "password2": "bar123",
        }
    )
    assert serializer.is_valid() == False

def test_user_serializer_pass_confirmation_validator(db):
    serializer = UserSignUpSerializer(
        data = {
            "username": "foo",
            "password1": "bar123$%",
            "password2": "bar123",
        }
    )
    assert serializer.is_valid() == False