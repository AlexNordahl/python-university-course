def make_ruler(n: int) -> None:
    dotts = "|"
    numbers = "0"
    segment_size = 5

    for i in range(n):
        dotts += "....|"
        if (i == 0):
            continue
        numbers += (" " * (segment_size - len(str(i)))) + str(i)

    numbers += (" " * (segment_size - len(str(n)))) + str(n)

    print(dotts + "\n" + numbers)

def make_grid(rows, cols):
    output = ""

    for k in range(cols):
        output += "+"
        for i in range(rows):
            output += "---+"

        output += "\n|"

        for j in range(rows):
            output += " " * 3 + "|"
        
        output += "\n"

    output += "+"
    for i in range(rows):
            output += "---+"

    print(output)

make_grid(4, 5)