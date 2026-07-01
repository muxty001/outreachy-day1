from user import get_user_status
from calculator import safe_divide

def run_application() -> None:
    """
    The main entry point that coordinates our system utilities.
    """
    print("--- Starting System Diagnostics ---")
    

    sample_user = {"name": "Dev", "is_active": True}
    user_message = get_user_status(sample_user)
    print(user_message)
    
   
    calculation_result = safe_divide(100, 5)
    print(f"Diagnostic Score: {calculation_result}")


if __name__ == "__main__":
    run_application()