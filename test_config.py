from config import upgrade_user_role

def test_successful_role_upgrade():
   
    starting_config = {
        "alice": "user",
        "bob": "guest"
    }
    
  
    updated_config = upgrade_user_role(starting_config, "alice")
    
   
    assert updated_config["alice"] == "admin"
    assert updated_config["bob"] == "guest"