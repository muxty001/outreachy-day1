from typing import Dict, Any

def upgrade_user_role(system_config: Dict[str, Any], username: str) -> Dict[str, Any]:
    """
    Takes a configuration dictionary and upgrades a specific user's role to 'admin'.
    """

    if username in system_config: 
        
        system_config[username] = 'admin'

        

    return system_config
