#1
bug = {}
for i in range(1, 6):
    bugs = int(input("Enter the number of bugs found on day {}: ".format(i)))
    bug[f"day_{i}"] = bugs
    total_bugs = sum(bug.values())
    print("Total bugs found after day {}: {}".format(i, total_bugs))

#2
calories = {}
for i in range(10, 31, 5):
    minutes_exercised = i
    calories[f"exercise_{i}"] = minutes_exercised

    total_calories = sum(calories.values()) * 4.2
    print("Total calories burned after exercise {}: {}".format(
        i, total_calories
    ))

#3
speed = float(input("Enter the vehicle's speed in miles per hour: "))
hours = int(input("Enter the number of hours traveled: "))

print("Hour\tDistance Traveled")

for hour in range(1, hours + 1):
    distance = speed * hour
    print(f"{hour}\t{distance} miles")

#4
years = int(input("Enter the number of years: "))
total_rainfall = 0
months = 0

for year in range(1, years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for year {year}, month {month}: "))
        total_rainfall += rainfall
        months += 1

average_rainfall = total_rainfall / months

print(f"Number of months: {months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f}")

#5
celsius = {}
for i in range(0, 21):
    celsius[f"celsius_{i}"] = i

for i in range(0, 21):
    fahrenheit = (celsius[f"celsius_{i}"] * 9/5) + 32
    print(f"{celsius[f'celsius_{i}']}°C = {fahrenheit}°F")

#6
days = int(input("Enter the number of days: "))
total_pay = 0.0

for day in range(1, days + 1):
    pay = float(input(f"Enter the money earned for day {day} out of {days}: "))
    total_pay += pay

print(f"Number of days: {days}")
print(f"Total pay: {total_pay:.2f}")
print(f"Average pay per day: {total_pay / days:.2f}")


#7
starting_weight = float(input("Enter your starting weight: "))

for months in range(1, 7):
    starting_weight -= 4.5
    weight_loss = round(starting_weight, 2)
    print(f"Month {months}: {weight_loss} pounds")

#8
for row in range(1, 9):
    for column in range(1, 9 - row):
        print("*", end="")
    print()

#9
n = 6
for i in range(n):
  
    for j in range(n - i - 1):
        print(' ', end='')
    print('#', end='')
    for k in range(i):
        print(' ', end='')
    print('#')
