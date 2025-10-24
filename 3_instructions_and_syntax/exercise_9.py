sequences = [[],[4],(1,2),[3,4],(5,6,7)]

output = []
for s in sequences:
    suma = 0
    for num in s:
        suma += num
    output.append(suma)

print(output)
