import random
#Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold.
num_numbers = int(input("How many random numbers do you want to generate? "))

try:
    with open("random_numbers.txt", "w") as file:
        for i in range(num_numbers):
            random_number = random.randint(1, 500)
            file.write(str(random_number) + "\n")

    with open("random_numbers.txt", "r") as file:
        lines = file.read().splitlines()
except IOError as error:
    print(f"An error occurred while accessing the file: {error}")
else:
    try:
        numbers = [int(line) for line in lines]
    except ValueError as error:
        print(f"Could not convert a line in the file to a number: {error}")
    else:
        for index, number in enumerate(numbers, start=1):
            print(f"Line {index}: {number}")

        print(f"Total of all numbers: {sum(numbers)}")