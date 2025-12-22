def generate_fibonacci(count):
    result = []
    a, b = 0, 1
    for _ in range(count):
        result.append(a)
        temp = a + b
        a, b = b, temp
    return result