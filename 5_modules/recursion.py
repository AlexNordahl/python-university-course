def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    result = 1
    for num in range(2, n + 1):
        result *= num
    
    return result

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