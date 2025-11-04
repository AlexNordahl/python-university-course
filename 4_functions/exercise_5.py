def reverse(L: list, left: int, right: int) -> list:
    if (len(L) <= left or len(L) <= right):
        return []

    while (left < right):
        L[left], L[right] = L[right], L[left]

        left += 1
        right -= 1

    return L

assert reverse([1, 2, 3, 4, 5, 6], 0, 5) == [6, 5, 4, 3, 2, 1]
assert reverse([1, 2, 3, 4, 5, 6], 6, 5) == []
assert reverse([1, 2, 3, 4, 5, 6], 3, 5) == [1, 2, 3, 6, 5, 4]
assert reverse([1, 2, 3, 4, 5, 6], 3, 3) == [1, 2, 3, 4, 5, 6]
assert reverse([1, 2, 3, 4, 5, 6], 5, 3) == [1, 2, 3, 4, 5, 6]