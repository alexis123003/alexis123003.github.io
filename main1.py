#1 
#input
option = int(input("Enter a number between 1 and 7: "))
#output and process

if option == 1:
    print("You chose monday")
elif option == 2:
    print("You chose tuesday")
elif option == 3:
    print("You chose wednesday")
elif option == 4:
    print("You chose thursday")
elif option == 5:
    print("You chose friday")
elif option == 6:
    print("You chose saturday")
elif option == 7:
    print("You chose sunday")
else:
    print("Please enter a different number between 1 and 7.")
#2
one_rect_l = float(input("Enter the length of the first rectangle: "))
one_rect_w = float(input("Enter the width of the first rectangle: "))
two_rect_l = float(input("Enter the length of the second rectangle: "))
two_rect_w = float(input("Enter the width of the second rectangle: "))
if(one_rect_l > two_rect_l or one_rect_w > two_rect_w):
    print("The first rectangle has a greater area than the second rectangle.")
elif(one_rect_l < two_rect_l  or one_rect_w < two_rect_w):
    print("The second rectangle has a greater area than the first rectangle.")
else:
    print("The two rectangles have the same area.")
#3
age = float(input("What is your age: "))
if(age >= 0 and age <= 1):
    print("👶 You are an infant")
elif(age > 1 and age < 13):
    print("👧 🧒 You are a child")
elif(age >= 13 and age < 20):
    print("👦 👩 You are a teenager")
elif(age >= 20):
    print("👩‍🦰 🧔You are an adult")
else:
    print("Please enter a valid age")
#5

mass = float(input("Enter your mass in kg: "))
weight = mass * 9.8
if(weight > 500):
    print("the object is too heavy")
elif(weight < 100):
    print("the object is too light")
else:
    print("the object is a good weight")
#6
month = int(input("Enter the date of the month : "))
day = int(input("Enter the date of the day : "))
year = int(input("Enter the last 2 digits of the year : "))
if(month * day == year):
    print("The date is magic")
else: 
    print("The date is not magic")

#10
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))
if(pennies+nickels*5+dimes*10+quarters*25 == 100):
    print("Congratulations! You have exactly one dollar.")
elif(pennies+nickels*5+dimes*10+quarters*25 > 100):
    print("You have more than one dollar.")
else:
    print("You have less than one dollar.")

#11
books = int(input("Enter the number of books purchased this month: "))
if(books == 0):
    print("You have not earned any points this month.")
elif(books == 2):
    print("You have earned 5 points this month.")
elif(books == 4):
    print("You have earned 15 points this month.")
elif(books == 6):
    print("You have earned 30 points this month.")
else:
    print("You have earned 60 points this month.")

#12
package = int(input("Enter the quantity of packages purchased: "))
if(package < 10):
    print(f"You have no discount.")
elif(package >= 10 and package <= 19):
    print(f"You have earned a 10% discount.")
elif(package >= 20 and package <= 49):
    print(f"You have earned a 20% discount.")
elif(package >= 50 and package <= 99):
    print(f"You have earned a 30% discount.")
else:
    print(f"You have earned a 40% discount.")

#15
seconds = int(input("Enter the number of seconds: "))
if(seconds < 60):
    print(f"{seconds} seconds is less than a minute.")
elif (seconds >= 60 and seconds < 3600):
    minutes = seconds // 60
    print(f"{seconds} seconds is equal to {minutes} minutes.")
elif (seconds >= 3600 and seconds < 86400):
    hours = seconds // 3600
    print(f"{seconds} seconds is equal to {hours} hours.")
else:
    days = seconds // 86400
    print(f"{seconds} seconds is equal to {days} days.")
