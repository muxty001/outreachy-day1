import os
import shutil
from session_manager import save_user_session

def test_session_missing_token():
    if "APP_AUTH_TOKEN" in os.environ:
        del os.environ["APP_AUTH_TOKEN"]
        
    result = save_user_session({"username": "developer_pro"})
    assert "Error" in result

def test_session_success_and_cleanup():
    os.environ["APP_AUTH_TOKEN"] = "secure_jwt_123"
    result = save_user_session({"username": "developer_pro"})
    
    # Assertions
    assert result == "Session Saved"
    assert os.path.exists("sessions/active_user.json")
    if os.path.exists("sessions"):
        shutil.rmtree("sessions") 
        
    del os.environ["APP_AUTH_TOKEN"]