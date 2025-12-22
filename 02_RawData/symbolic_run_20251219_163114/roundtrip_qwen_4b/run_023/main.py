def generate_fibonacci(n):
    result = 0
    a = 1
    b = 2
    while n > 0:
        result += a
        n -= 1
        a += b
        b += a
    return result