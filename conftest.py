import pytest
import requests
import re
from faker import Faker

fake = Faker()

BASE_URL = 'http://localhost:28080/rs/users'
FIRST_NAME = fake.first_name()
LAST_NAME = fake.last_name()


def create_new_user(first_name, last_name):
    response = requests.post(BASE_URL, data={'firstName': first_name, 'lastName': last_name})
    return {'first_name': first_name, 'last_name': last_name, 'response': response}


def get_all_users():
    return requests.get(BASE_URL)


def parse_resp(resp):
    m = []
    pattern = re.compile('ID=(\d*), FIRSTNAME=(\w*), LASTNAME=(\w*)')
    f = pattern.findall(resp)
    fields = ('id', 'first_name', 'last_name')
    for i in f:
        m = [dict(zip(fields, i)) for j in range(len(f))]
    return m


@pytest.fixture(scope='function', params=[
    (FIRST_NAME, LAST_NAME),
    (FIRST_NAME, ''),
    ('', LAST_NAME), ('', '')
], ids=['With first name & last name', 'With only first name', 'With only last name', 'With nothing'])
def param_test(request):
    return request.param
