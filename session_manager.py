import os
import json
from typing import Dict, Union

def save_user_session(session_data: Dict) -> str:
    """
    Safely takes session metadata, reads an app token,
    creates the output directory if missing, and writes the JSON.
    """
    try:
        token = os.environ.get("APP_AUTH_TOKEN")
        if not token:
            return "Error: APP_AUTH_TOKEN environment variable is missing."
            
        session_data["auth_token"] = token
        os.makedirs("sessions", exist_ok=True)
        with open("sessions/active_user.json", "w", encoding="utf-8") as file:
            json.dump(session_data, file, indent=4)
            
        return "Session Saved"
        
    except (OSError, TypeError) as error:
        return f"Error: Could not save session. Details: {error}"