
def process_data(value: int) -> int:
    """
    Simulates a data processing function.
    
    This function has a bug where it will fail if a non-integer value is passed.
    """
    return value + 100

if __name__ == "__main__":
    try:
        result = process_data("100")
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error caught: {e}")
