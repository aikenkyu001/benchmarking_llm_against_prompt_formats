python
from main import generate_fibonacci

def main():
    count = 0
    result = []
    a = 0
    b = 1
    while count < 10:
        temp = a + b
        a = b
        b = temp
        count += 1
        result.append(count)
    return result