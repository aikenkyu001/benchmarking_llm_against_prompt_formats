def generate_fibonacci(n):
  """Generates the first n Fibonacci numbers."""
  a = 0
  b = 1
  for i in range(n):
    a, b = b, a + b
  return a

def test_generate_fibonacci(n):
  """Generates the first n Fibonacci numbers."""
  a = 0
  b = 1
  for i in range(n):
    a, b = b, a + b
  return a