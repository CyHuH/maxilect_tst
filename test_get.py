from conftest import get_all_users


def test_get_users():
    users = get_all_users()
    assert users.status_code == 200
