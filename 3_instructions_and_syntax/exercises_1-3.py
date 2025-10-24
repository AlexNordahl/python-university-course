# -- exercise 1 --

# Python is not C, using semicolon generates syntax error.
# x = 2; y = 3; 
# if (x > y):
#     result = x;
# else:
#     result = y;

# Indentation is critical, it marks code segments,
# without it there will be syntax error.
# for i in "axby": if ord(i) < 100: print (i)

# Making one-line loops and if's is ok.
# for i in "axby": print (ord(i) if ord(i) < 100 else i)

# -- exercise 2 --

# sort() sorts in-place and returns None
# L = [3, 5, 4] ; L = L.sort()

# too many values to unpack, expected 2
# x, y = 1, 2, 3

# X is a tuple, tuples are immutable
# X = 1, 2, 3 ; X[1] = 4

# Index out of bounds, porper indexing: (0, len(X) - 1)
# X = [1, 2, 3] ; X[3] = 4

# strings in python are immutable
# X = "abc" ; X.append("d")

# pow requires 2 arguments, we can add second range(8)
# or fix it with lambda
# L = list(map(pow, range(8)))

# -- exercise 3 --

def print_nums()
    for num in range(31):
        if (num % 3 != 0):
            print(num, end=" ")
    print()