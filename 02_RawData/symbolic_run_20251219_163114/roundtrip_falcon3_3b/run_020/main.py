def generate_fibonacci(count):
    result = []
    a = 0
    b = 1
    
    for _ in range(count):
        temp = a + b
        a = b
        b = temp
        result.append(a)
    
    return result