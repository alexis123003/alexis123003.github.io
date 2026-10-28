# Complete the following chapter 6 exercises in repl.it. You will submit the links to your finished programs.

# Robot Olympics Club
# The Robot Olympics Club has a tournament every weekend. The club president has asked you to write two programs:
# A program that will read each team's name and Robo Rank Score (RRS) as keyboard input, then save these as records in a file named robo.txt.
# A program that reads the records from the robo.txt file and displays them.

print("Robot Olympics Club")

tournament = int(input("How many teams do you want to record? "))

with open("robo.txt", "w") as robo:
    for i in range(1, tournament + 1):
        team_name = input(f"{i}. Enter the team name: ")
        rrs = input(f"{i}. Enter the team RRS: ")
        robo.write(f"{team_name},{rrs}\n")

print("Here are the saved team records:")
with open("robo.txt", "r") as robo:
    for line in robo:
        team_name, rrs = line.strip().split(",")
        print(f"Team Name: {team_name}, RRS: {rrs}")

# Data Mining
# The NSA is monitoring your activities including how many times you say the word "the" each day.
# Write a program that generates 365 numbers and writes them into a file, the.txt, one number per line.
# This will be the number of times you have said "the" each day in 2020.
go_on = input("input Enter to generate the data for the year 2020...")

if go_on.lower() == "enter" or go_on.lower() == "Enter":
    import random

    with open("the.txt", "w") as the_file:
        for day in range(365):
            count = random.randint(0, 100)
            the_file.write(f"{count}\n")

    with open("the.txt", "r") as read:
        print("The file the.txt has been created with 365 daily counts.")
        print("December average \"the\"s :", read.read())
    