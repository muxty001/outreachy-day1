from typing import Dict, Any


def get_user_status(user_data: Dict[str, Any]) -> str:
    """Safely extracts user details and returns a formatted status string."""
    
  
    name = user_data.get("name", "Anonymous")
    is_active = user_data.get("is_active", False)

   
    if is_active:
       
        return f"User {name} is currently active."

  
    return f"User {name} is inactive."