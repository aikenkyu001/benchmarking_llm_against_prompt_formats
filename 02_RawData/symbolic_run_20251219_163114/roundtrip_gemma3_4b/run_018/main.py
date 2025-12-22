def generate_fibonacci(count):
    result = []
    a = 0
    b = 1
    while count > 0:
        result.append(a)
        temp = a + b
        a = b
        b = temp
        count -= 1
    return result