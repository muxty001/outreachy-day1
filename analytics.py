def process_numbers(numbers):
    """
    Takes a list of numbers, filters out the odd numbers,
    and returns a list of the even numbers squared.
    """
    # This is a Python List Comprehension - idiomatic and fast!
    return [x**2 for x in numbers if x % 2 == 0]