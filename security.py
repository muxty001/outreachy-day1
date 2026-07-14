import os
from typing import Union

def get_api_access_token() -> Union[str, bool]:
    """
    Safely retrieves the system environment variable 'API_SECRET_KEY'.
    Returns the token string if found, or False if the configuration is missing.
    """
    token = os.environ.get("API_SECRET_KEY")
    
    if not token:
        return False
        
    return f"Bearer {token}"