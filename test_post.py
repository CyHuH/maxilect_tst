from conftest import parse_resp, create_new_user


def test_create_user(param_test):
    (first_name, last_name) = param_test
    new_user = create_new_user(first_name, last_name)
    assert new_user['response'].status_code == 200
    result = parse_resp(new_user['response'].text)
    assert result[0]['first_name'] == new_user['first_name']
    assert result[0]['last_name'] == new_user['last_name']
