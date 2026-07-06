from typing import List, Union


def process_numbers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Takes a list of numbers, filters out the odd numbers,
    and returns a list of the even numbers squared.
    """
    
    return [x**2 for x in numbers if x % 2 == 0]