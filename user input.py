user_input = input("Please enter a number: ")

# check if the input is a positive integer
if user_input.isnumeric() and int(user_input) > 0:
    print("You have entered a natural number.")
else:
    print("You have not entered a natural number.")
