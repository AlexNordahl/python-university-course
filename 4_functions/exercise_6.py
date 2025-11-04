def sum_seq(seq):
    result = 0
    
    for item in seq:
        if not isinstance(item, (list, tuple)):
            result += item
        else:
            for number in item:
                result += number
    
    return result

assert sum_seq([1, 2, 3, (1, 2, 3), [4, 5]]) == 21
assert sum_seq([[1, 2, 3], (1, 2, 3)]) == 12
assert sum_seq(([1, 2, 3], (1, 2, 3))) == 12