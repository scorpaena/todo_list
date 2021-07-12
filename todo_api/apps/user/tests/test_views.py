import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def user(db):
    return User.objects.create_user(
        username = 'foo',
        password = 'bar123$%',
    )

@pytest.fixture
def api_client():
    return APIClient


def test_user_signup(db, api_client):
    response = api_client().post('/user/signup/',
        data = {
            "username": "foo",
            "password1": "bar123$%",
            "password2": "bar123$%",
        }
    )
    assert response.status_code == 201
    assert User.objects.last().id == 1

def test_user_login(api_client, user):
    response = api_client().post('/user/login/',
        data = {
            "username": "foo",
            "password": "bar123$%",
        }
    )
    assert response.status_code == 200
    assert response.data["success"] == "you are logged in"

def test_user_logout(api_client, user):
    response = api_client().get('/user/logout/')
    assert response.status_code == 200
    assert response.content.decode("utf-8") == "you are logged out"
