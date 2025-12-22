def generate_fibonacci():
    result = []
    a, b = 0, 1
    for _ in range(2):
        result.append(a)
        temp = a + b
        a, b = b, temp
    return result