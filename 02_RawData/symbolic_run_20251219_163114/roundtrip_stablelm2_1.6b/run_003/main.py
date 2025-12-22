python
def generate_fibonacci(count):
    result = 0
    a = 0
    b = 1

    for _ in range(count):
        result += a
        a, b = b, result + b
    return result


if __name__ == "__main__":
    count = int(input("Enter the count: "))
    fibonacci_result = generate_fibonacci(count)

    print(f"The {count}th Fibonacci number is: {fibonacci_result}")