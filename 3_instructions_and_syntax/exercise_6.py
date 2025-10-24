x = int(input("enter x: "))
y = int(input("enter y: "))

output = ""

for k in range(y):
    output += "+"
    for i in range(x):
        output += "---+"

    output += "\n|"

    for j in range(x):
        output += " " * 3 + "|"
    
    output += "\n"

output += "+"
for i in range(x):
        output += "---+"

print(output)