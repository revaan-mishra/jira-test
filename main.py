# A simple function with a known bug to simulate a real-world issue.
# This code is "buggy" because it expects an integer but fails if a string is provided.
def process_data(value: int) -> int:
    """
    Simulates a data processing function.
    
    This function has a bug where it will fail if a non-integer value is passed.
    """
    return value + 100

if __name__ == "__main__":
    # This is a sample run that would produce an error with a string input
    try:
        result = process_data("100")
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error caught: {e}")
