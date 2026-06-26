from typing import List, Dict, Any


def get_active_usernames(users: List[Dict[str, Any]]) -> List[str]:
    """
    Takes a list of user dictionaries, filters for active users, 
    and returns their names sorted alphabetically.
    """
    active_names: List[str] = []

    for user in users:
        if user.get("is_active", False):
            name = user.get("name", "Anonymous")   
            active_names.append(name)


    active_names.sort()  
    return active_names  