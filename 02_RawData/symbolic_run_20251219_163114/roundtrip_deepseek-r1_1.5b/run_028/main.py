def generate_fibonacci(count):
    a = 0
    b = 1
    for _ in range(count):
        temp = a + b
        a = b
        b = temp
    return a + b