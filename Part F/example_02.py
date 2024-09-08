# Performance Optimization

# Old Version: A loop that iterates over a large dataset multiple times
def find_common_elements_old(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

# New Version: Using a set for efficient lookups
def find_common_elements_new(list1, list2):
    set1 = set(list1)
    return [item for item in list2 if item in set1]

# Example usage
large_list1 = list(range(10000))
large_list2 = list(range(5000, 15000))

# Old version (slower)
import time

start_time = time.time()
result_old = find_common_elements_old(large_list1, large_list2)
end_time = time.time()
print(f"Old version time: {end_time - start_time:.6f} seconds")
print(f"Number of common elements (old): {len(result_old)}")

# New version (faster)
start_time = time.time()
result_new = find_common_elements_new(large_list1, large_list2)
end_time = time.time()
print(f"New version time: {end_time - start_time:.6f} seconds")
print(f"Number of common elements (new): {len(result_new)}")