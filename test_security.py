import os
from security import get_api_access_token

def test_token_missing():
    if "API_SECRET_KEY" in os.environ:
        del os.environ["API_SECRET_KEY"]
        
    assert get_api_access_token() is False

def test_token_present():
    os.environ["API_SECRET_KEY"] = "super-secret-dev-token-123"
    assert get_api_access_token() == "Bearer super-secret-dev-token-123"
    del os.environ["API_SECRET_KEY"]