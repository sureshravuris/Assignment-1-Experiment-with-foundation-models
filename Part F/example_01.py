# Code Refactoring for Readability


# Original Fibonacci function
def fibonacci(n):
    """
    Calculate the nth Fibonacci number iteratively.
    
    :param n: The position of the Fibonacci number to calculate
    :return: The nth Fibonacci number
    """
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Refactored Fibonacci function using recursion
def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number recursively.
    
    :param n: The position of the Fibonacci number to calculate
    :return: The nth Fibonacci number
    """
    # Base cases
    if n <= 1:
        return n
    
    # Recursive case
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Explanation of refactoring:
"""
The original 'fibonacci' function was refactored into 'fibonacci_recursive' to use recursion.
Here's how the refactoring was done:

1. Base cases:
   - Both functions handle the base cases (n <= 1) similarly, returning n directly.

2. Main logic:
   - Original: Uses a loop to iteratively calculate Fibonacci numbers.
   - Refactored: Uses recursion to calculate Fibonacci numbers.

3. Recursive approach:
   - The recursive function calls itself with smaller inputs (n-1 and n-2).
   - It combines these recursive calls to compute the nth Fibonacci number.

4. Performance consideration:
   - While the recursive version is more concise and arguably more intuitive,
     it's less efficient for large n due to repeated calculations.
   - The original iterative version is more efficient for large n.

5. Readability:
   - The recursive version directly translates the mathematical definition 
     of Fibonacci numbers, which can be easier to understand at a glance.

Both implementations are correct, but they showcase different programming paradigms
and have different performance characteristics.
"""

# Example usage
if __name__ == "__main__":
    n = 10
    print(f"The {n}th Fibonacci number (iterative): {fibonacci(n)}")
    print(f"The {n}th Fibonacci number (recursive): {fibonacci_recursive(n)}")