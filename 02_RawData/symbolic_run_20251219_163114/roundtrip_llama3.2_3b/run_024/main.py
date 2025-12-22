def generate_fibonacci(count):
    result = 0
    a = 0
    b = 1
    while True:
        temp = a + b
        a = b
        b = temp
        if b == count:
            return result
        result += 1