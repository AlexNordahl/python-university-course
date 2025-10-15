# exercise 1

def get_number_of_words(string):
    return len((string.strip()).split())

words = " abc " * 5
assert get_number_of_words(words) == 5, "get_number_of_words doesn't work as expected"

# exercise 2

def to_snake(string):
    string = string.strip().replace(" ", "_")
    return string

words = "abc " * 3
assert to_snake(words) == "abc_abc_abc", "to_snake doesn't work"

# exercise 3