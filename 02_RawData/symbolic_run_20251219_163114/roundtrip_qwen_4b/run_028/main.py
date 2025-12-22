def generate_fibonacci(count):
    result = 0
    a = 1
    b = 2
    while count > 0:
        result += a
        count -= 1
        a += b
        b += a
    return result

generate_fibonacci(10))