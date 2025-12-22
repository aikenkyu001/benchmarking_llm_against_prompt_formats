def generate_fibonacci(count):
    result = []
    a = 0
    b = 1
    for _ in range(count):
        result.append(a)
        temp = a + b
        a = b
        b = temp
    return result