# Improving Function Documentation

def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    This function takes the length and width of a rectangle and returns its area.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.

    Example:
    >>> calculate_area(5, 3)
    15.0
    """
    return length * width

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    This function determines whether the given number is prime or not.
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.

    Example:
    >>> is_prime(17)
    True
    >>> is_prime(4)
    False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.

    This function returns the nth number in the Fibonacci sequence using recursion.
    The Fibonacci sequence is defined as: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.

    Parameters:
    n (int): The position in the Fibonacci sequence to calculate (0-indexed).

    Returns:
    int: The nth Fibonacci number.

    Note:
    This recursive implementation may be slow for large values of n.
    Consider using an iterative approach for better performance with large inputs.

    Example:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(6)
    8
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)