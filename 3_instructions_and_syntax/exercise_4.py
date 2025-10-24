print("Enter stop to exit")
while (True):
    user_input = input("Please enter number: ")

    if user_input == "stop":
        print("Bye")
        break

    if not user_input.isnumeric():
        print("That's no a number!")
        continue
    
    number = float(user_input)

    print("number = {0}, number ** 3 = {1}".format(number, number ** 3))