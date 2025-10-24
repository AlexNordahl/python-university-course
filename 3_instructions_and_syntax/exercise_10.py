# method 1
roman = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])
print(roman)

# method 2
roman_2 = {}
for key, value in roman.items():
    roman_2[key] = value
print(roman_2)

# method 3
roman_3 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}