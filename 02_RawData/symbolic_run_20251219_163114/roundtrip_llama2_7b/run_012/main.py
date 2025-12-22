def generate_fibonacci(count):
    result = 0
    a = 0
    b = 1
    temp = 0
    
    for _ in range(count):
        temp = a + b
        a = b
        b = temp
        result += 1
    
    return result

---