from calculator import safe_divide

def test_successful_division():
    assert safe_divide(10, 2) == 5.0

def test_divide_by_zero_edge_case():
    
    assert safe_divide(10, 0) == "Error: Cannot divide by zero."

def test_invalid_type_edge_case():
   
    assert safe_divide(10, "two") == "Error: Both inputs must be numeric numbers."