length = int(input("Please enter length: "))

dotts = "|"
numbers = "0"
segment_size = 5

for i in range(length):
    dotts += "....|"
    if (i == 0):
        continue
    numbers += (" " * (segment_size - len(str(i)))) + str(i)

numbers += (" " * (segment_size - len(str(length)))) + str(length)

print(dotts + "\n" + numbers)