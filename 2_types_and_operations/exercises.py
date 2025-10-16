# -- exercise 1 --

def get_number_of_words(string: str):
    return len((string.strip()).split())

words = " dhhbshda\n    \ndshjd "
assert get_number_of_words(words) == 2

# -- exercise 2 --

def to_snake(string: str):
    string = string.strip().replace(" ", "_")
    return string

words = "abc " * 3
assert to_snake(words) == "abc_abc_abc"

# -- exercise 3 --

def get_chrs(string: str, index = 0):
    words = string.strip().split()

    if (len(words) == 0):
        return ""

    return words[index]

words = "   abc\t def   \nghi   "
assert get_chrs(words) == "abc"
assert get_chrs(words, -1) == "ghi"

# -- exercise 4 --

def words_length(string: str):
    return len("".join(string.strip().split()))

assert words_length(words) == 9

# -- exercise 5 --

def longest_word(string: str):
    return max(string.strip().split(), key=len)

words = "   abc\t defdefdef   \nghi   "
assert longest_word(words) == "defdefdef"
assert len(longest_word(words)) == 9

# -- exercise 6 --

def ints_to_str(lst: list[int]):
    return "".join([str(num) for num in lst])

L = [1, 22, 33, 4, 5, 6, 78]
assert ints_to_str(L) == "1223345678"

# -- exercise 7 --

words = "defdGvRefdef"
assert words.replace("GvR", "Guido van Rossum") == "defdGuido van Rossumefdef"

# -- exercise 8 --

words = "   abc\t defdefdef   \nghi   "

assert sorted(words.strip().split()) == ['abc', 'defdefdef', 'ghi']
assert sorted(words.strip().split(), key=len) == ['abc', 'ghi', 'defdefdef']

# -- exercise 9 --

def count_zeroes(num: int):
    return str(num).count('0')

num = 920005700973123003210
assert count_zeroes(num) == 8

# -- exercise 10 --

def ints_to_blocked_str(lst: list[int]):
    result = ""
    for num in lst:
        result += str(num).zfill(3)
    
    return result


L = [3, 17, 82, 5, 104, 256, 9, 73, 999, 48, 120]
assert ints_to_blocked_str(L) == "003017082005104256009073999048120"