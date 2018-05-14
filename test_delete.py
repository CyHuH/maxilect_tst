import requests
from conftest import BASE_URL, FIRST_NAME, LAST_NAME, get_all_users, parse_resp, create_new_user


def test_delete_user():
    new_user = create_new_user(FIRST_NAME, LAST_NAME)
    assert new_user['response'].status_code == 200
    result = parse_resp(new_user['response'].text)
    user_id = result[0]['id']
    r = requests.delete(BASE_URL + '/' + user_id)
    assert r.status_code == 200
    r = get_all_users()
    result = parse_resp(r.text)
    assert result[-1]['id'] != user_id
    assert result[-1]['first_name'] != new_user['first_name']
    assert result[-1]['last_name'] != new_user['last_name']
