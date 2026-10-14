import random
file = input("Enter the filename: ")
if file == "one":
    with open("one.txt", "r") as file:
        for i, line in enumerate(file):
            if i < 5:
                print(i + 1, ":", line )
elif file == "two":
    with open("two.txt", "r") as file:
        for i, line in enumerate(file):
            if i < 5:
                print(i + 1, ":", line)
elif file == "three":
    with open("three.txt", "r") as file:
        for i, line in enumerate(file):
            if i < 5:
                print(i + 1, ":", line)
else:
    print("File not found.")
    # Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold.
    num_numbers = int(input("How many random numbers do you want to generate? "))
    