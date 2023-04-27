from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

def test_login_user(client, test_user):
    test_username, test_password = test_user  # this unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True
    """
    In this code, the client passed in as a parameter is a built-in "dummy web client" provided by Django as part of its testing tools.
It mimics some of the functionality of a web browser and helps us test interacting with a Django app. 
For more information, see: https://docs.djangoproject.com/en/3.2/topics/testing/tools/
Its login() method helps us test that we can log into the app, and the test_user fixture makes sure that we have a valid user to test with.
    """