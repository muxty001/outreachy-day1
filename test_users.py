from users import get_user_status

def test_active_user():
    user = {"name": "Alice", "is_active": True}
    assert get_user_status(user) == "User Alice is currently active."

def test_missing_keys():
    # If the API returns an empty dict, our code should still work, not crash.
    empty_user = {}
    assert get_user_status(empty_user) == "User Anonymous is inactive."