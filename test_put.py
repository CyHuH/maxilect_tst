import requests
import faker
from conftest import BASE_URL, get_all_users, parse_resp, create_new_user

fake = faker.Faker()
FIRST_NAME = fake.first_name()
LAST_NAME = fake.last_name()


def test_update_user(param_test):
    (new_first_name, new_last_name) = param_test
    new_user = create_new_user(FIRST_NAME, LAST_NAME)
    assert new_user['response'].status_code == 200
    result = parse_resp(new_user['response'].text)
    r = requests.put('{0}/{1}'.format(BASE_URL, result[0]['id']),
                     data={'firstName': new_first_name, 'lastName': new_last_name})
    assert r.status_code == 200
    users = get_all_users()
    resp = parse_resp(users.text)
    assert resp[-1]['first_name'] == new_first_name
    assert resp[-1]['last_name'] == new_last_name
