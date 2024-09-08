#Adding Type Annotations

# Old Version (without type hints):

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    num = 10
    result = fibonacci(num)
    print(f"The {num}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()

# New Version (with type annotations):

from typing import List

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def generate_fibonacci_sequence(length: int) -> List[int]:
    sequence: List[int] = []
    for i in range(length):
        sequence.append(fibonacci(i))
    return sequence

def main() -> None:
    num: int = 10
    result: int = fibonacci(num)
    print(f"The {num}th Fibonacci number is: {result}")

    sequence: List[int] = generate_fibonacci_sequence(num)
    print(f"Fibonacci sequence up to {num} terms: {sequence}")

if __name__ == "__main__":
    main()