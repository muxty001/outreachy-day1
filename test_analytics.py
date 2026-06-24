from analytics import process_numbers

def test_process_numbers():
    # Test with a mix of evens and odds
    assert process_numbers([1, 2, 3, 4, 5]) == [4, 16]
    
    # Test with an empty list
    assert process_numbers([]) == []
    
    # Test with all odd numbers
    assert process_numbers([1, 3, 5]) == []