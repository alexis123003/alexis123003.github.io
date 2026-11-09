name = input("Enter your first, middle, and last name: ")
name_parts = name.split()
print(f"{name_parts[0][0].title()}. {name_parts[1][0].title()}. {name_parts[2][0].title()}.")
print()
#Write a program that asks the user to enter a series of single-digit numbers with nothing separating them. The program should display the sum of all the single-digit numbers in the string. For example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4.
numbers = input("Enter a series of single-digit numbers with nothing separating them: ")
total = 0
for digit in numbers:
    if digit.isdigit() and 0 <= int(digit) <= 9:
        total += int(digit)
print(f"The sum of the single-digit numbers is: {total}")

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char.isalpha() and char not in vowels)

user_string = input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowels(user_string)}")
print(f"The number of consonants in the string is: {count_consonants(user_string)}")