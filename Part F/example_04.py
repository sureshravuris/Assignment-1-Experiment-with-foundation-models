# Improving Function Duplication


# Old version with code duplication

def process_data_for_department_a(data):
    # Preprocessing
    cleaned_data = [item.strip().lower() for item in data]
    
    # Processing specific to Department A
    result_a = [item + "_a" for item in cleaned_data]
    
    # Postprocessing
    final_result_a = [item.capitalize() for item in result_a]
    return final_result_a

def process_data_for_department_b(data):
    # Preprocessing
    cleaned_data = [item.strip().lower() for item in data]
    
    # Processing specific to Department B
    result_b = [item + "_b" for item in cleaned_data]
    
    # Postprocessing
    final_result_b = [item.capitalize() for item in result_b]
    return final_result_b

# Example usage (old version)
data = ["  Item1 ", "ITEM2", "item3  "]
result_a_old = process_data_for_department_a(data)
result_b_old = process_data_for_department_b(data)

print("Old Version - Department A:", result_a_old)
print("Old Version - Department B:", result_b_old)

print("\n" + "="*50 + "\n")

# New version with reduced code duplication

def preprocess_data(data):
    return [item.strip().lower() for item in data]

def postprocess_data(data):
    return [item.capitalize() for item in data]

def process_data_for_department(data, department):
    cleaned_data = preprocess_data(data)
    result = [f"{item}_{department}" for item in cleaned_data]
    return postprocess_data(result)

# Example usage (new version)
result_a_new = process_data_for_department(data, "a")
result_b_new = process_data_for_department(data, "b")

print("New Version - Department A:", result_a_new)
print("New Version - Department B:", result_b_new)