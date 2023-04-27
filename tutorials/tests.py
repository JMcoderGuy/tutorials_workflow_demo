from tutorials.models import Tutorial
from django.test import TestCase
from django.urls import reverse
import pytest
# Create your tests here.
# By providing a view name to the reverse() function, we can get the URL of the view.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"

# @pytest.mark.django_db 
# def test_create_tutorial():
#     tutorial = Tutorial.objects.create(
#         title='Pytest',
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#         description='Tutorial on how to apply pytest to a Django application',
#         published=True
#     )
#     assert tutorial.title == "Pytest"
"""
If you run above with pytest -k create without adding @pytest.mark.django_db 
above the def test_create_tutorial functiion, pytest will not have acess to the
database to run the test so it will FAIL, add @pytest.mark.django_db as a marker
to make it pass

"""

@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial
"""
This new_tutorials() fixture function will create a new tutorial object with the attributes described 
(a title of 'Pytest', etc) any time it is used as a parameter in a test function.
Then, in that test function, that tutorial object will be available to use under 
the same name as the function name, new_tutorial. Notice that new_tutorials() has the parameter db.
This is a built-in fixture provided by pytest-django. 
Like the marker @pytest.mark.django_db, this fixture is used by other fixture functions to 
get access to the connected database.
"""
def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk