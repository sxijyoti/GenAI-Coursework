def calculate_area(length, width):
    return length * width

def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def reverse_string(s):
    return s[::-1]

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def read_file_lines(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]