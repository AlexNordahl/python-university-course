def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    result = 1
    for num in range(2, n + 1):
        result *= num
    
    return result

assert factorial(3) == 6
assert factorial(6) == 720
assert factorial(12) == 479001600