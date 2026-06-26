from directory import get_active_usernames

def test_active_usernames_sorting():
   
    raw_users = [
        {"name": "Charlie", "is_active": True},
        {"name": "Alice", "is_active": True},
        {"name": "Bob", "is_active": False},  
        {"name": "David", "is_active": True}
    ]
    
   
    assert get_active_usernames(raw_users) == ["Alice", "Charlie", "David"]

def test_empty_directory():
    assert get_active_usernames([]) == []