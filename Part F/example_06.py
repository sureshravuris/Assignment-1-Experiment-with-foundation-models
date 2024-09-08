# Error Handling Enhancement

import logging

# Old Version: Function with bare except
def old_divide_numbers(a, b):
    try:
        result = a / b
        return result
    except:
        print("An error occurred")
        return None

# New Version: Function with specific exception handling and error logging
logging.basicConfig(level=logging.ERROR)

def new_divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        return None
    except TypeError:
        logging.error("Invalid type for division operation")
        return None
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    print("Old Version:")
    print(old_divide_numbers(10, 2))
    print(old_divide_numbers(10, 0))
    print(old_divide_numbers("10", 2))

    print("\nNew Version:")
    print(new_divide_numbers(10, 2))
    print(new_divide_numbers(10, 0))
    print(new_divide_numbers("10", 2))