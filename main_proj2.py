first_name = input("What is your first name?")
first_i = input("What is your first initial?")
last_i = input("What is your last initial?")
first_number = input("Please enter a number")
first_number = int(first_number)
second_number = input("Please enter another number")
second_number = int(second_number)

one = first_number + second_number
two = first_number - second_number
three = first_number *second_number
four = first_number / second_number

print(f"Your name is {first_name}, {first_i}{last_i} and the numbers you chose were {first_number} and {second_number}.\n The sum of the two numbers is {one}.\n The difference is {two}.\n The product is {three}.\n And the quotient is {four:.2f}.")
