from typing import Union


def safe_divide(numerator: Union[int, float], denominator: Union[int, float]) -> Union[int, float, str]:
    """
    Safely divides two numbers and handles exceptions gracefully.
    """
    
    try:
        return numerator / denominator
        
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    
    except TypeError:
        return "Error: Both inputs must be numeric numbers."