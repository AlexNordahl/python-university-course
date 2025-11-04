def fibonacci(n: int) -> int:
    if n in (1, 2):
        return n - 1

    first, second = 0, 1
    next_fib = 0

    for _ in range(2, n):
        next_fib = first + second
        first = second
        second = next_fib

    return next_fib

assert fibonacci(3) == 1
assert fibonacci(4) == 2
assert fibonacci(5) == 3
assert fibonacci(6) == 5