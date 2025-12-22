def generate_fibonacci(count):
    result = 0
    a = 0
    b = 1
    for _ in range(count):
        temp = a + b
        a = b
        b = temp
    return [a, *range(a+1, b+1)]python