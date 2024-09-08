# Reducing Code Duplication
import time
import random

# Generate a large dataset
data = [random.randint(1, 1000000) for _ in range(1000000)]
target = random.randint(1, 1000000)

def old_version():
    """
    Old Version: A loop that iterates over a large dataset multiple times.
    """
    print("Old Version: Iterating over the dataset multiple times")
    
    found = False
    iterations = 0
    
    start_time = time.time()
    
    for _ in range(10):  # Simulating multiple iterations over the dataset
        for item in data:
            iterations += 1
            if item == target:
                found = True
                break
        if found:
            break
    
    end_time = time.time()
    
    print(f"Target {'found' if found else 'not found'}")
    print(f"Number of iterations: {iterations}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

def new_version():
    """
    New Version: Using a set for efficient lookup.
    """
    print("\nNew Version: Using a set for efficient lookup")
    
    start_time = time.time()
    
    # Convert the list to a set for O(1) lookup
    data_set = set(data)
    
    found = target in data_set
    
    end_time = time.time()
    
    print(f"Target {'found' if found else 'not found'}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    print("Performance Optimization Example")
    print("================================")
    
    old_version()
    new_version()

    print("\nExplanation:")
    print("The old version uses nested loops to iterate over the dataset multiple times,")
    print("resulting in a time complexity of O(n^2) in the worst case.")
    print("The new version converts the list to a set, which allows for O(1) lookup time,")
    print("significantly reducing the overall time complexity to O(n) for the conversion")
    print("plus O(1) for the lookup.")