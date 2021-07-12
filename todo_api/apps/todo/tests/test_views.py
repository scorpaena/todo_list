import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.todo.models import ToDo

@pytest.fixture
def user(db):
    return User.objects.create_user(
        username = 'foo',
        password = 'bar123$%',
    )

@pytest.fixture
def todo(db, user):
    return ToDo.objects.create(
        title = 'title',
        description = 'description',
        user = user,
    )

@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


def test_todo_list(api_client, todo):
    response = api_client.get('/todo/')
    assert response.status_code == 200
    assert response.data['count'] == 1

def test_todo_create(api_client, todo):
    response = api_client.post('/todo/',
        data = {
            "title": "title_create",
            "description": "description_create",
            "user": user,
        }
    )
    assert response.status_code == 201
    assert ToDo.objects.last().title == "title_create"

def test_todo_retrieve(api_client, todo):
    response = api_client.get('/todo/{pk}/'.format(pk=todo.id))
    assert response.status_code == 200
    assert response.data["title"] == todo.title

def test_todo_update(api_client, todo):
    response = api_client.put('/todo/{pk}/'.format(pk=todo.id),
        data = {
            "title": "title_update",
            "description": "description_update",
            "user": user,
        }
    )
    assert response.status_code == 200
    assert ToDo.objects.last().title == "title_update"

def test_todo_destroy(api_client, todo):
    response = api_client.delete('/todo/{pk}/'.format(pk=todo.id))
    assert response.status_code == 204
    assert ToDo.objects.all().count() == 0