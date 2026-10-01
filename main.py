import random

#1 Write a program that asks the user to enter a distance in kilometers,
# then converts that distance to miles.

kilometers = float(input("Enter a distance in kilometers: "))
miles = kilometers * 0.6214
print(f"The distance in miles is: {miles}")

#2 Many financial experts advise that property owners should insure their homes
# or buildings for at least 80 percent of the amount it would cost to replace
# the structure.

replacement_cost = float(input("Enter the replacement cost of a building: "))
insurance_amount = replacement_cost * 0.80
print(f"The minimum amount of insurance that covers {replacement_cost} is: ${insurance_amount:,.2f}")
#3 Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of these expense

loan_payment = float(input("enter the monthly costs for the loan payments: "))
insurance_car =float(input("enter the monthly costs for the car insurance: "))
gas = float(input("enter the monthly costs for the Gas: "))
oil = float(input("enter the monthly costs for the oil: "))
tires = float(input("enter the monthly costs for the tires: "))
maintenance = float(input("enter the monthly costs for the maintenance: "))
amount_total = loan_payment + insurance_car +gas +oil +tires + maintenance
print(f"total monthly cost of these expenses: {amount_total}")
print(f"Yearly amount: {amount_total * 12}")

#5 Calories from Fat and Carbohydrates A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula: 
# caloriesfromfat=fatgrams×9 Next, she calculates the number of calories that result from the carbohydrates, using the following formula: caloriesfromcarbs=carbgrams×4 The nutritionist asks you to write a program that will make these calculations.
fat = float(input("Enter how much Fat grams you consumed in a day"))
carbs = float(input("Enter how much carbohydrate grams you consumed in a day")) 
caloriesfromfat = fat * 9
caloriesfromcarbs =carbs * 4
print(f"calories from fat: {caloriesfromfat} Calories from carbs: {caloriesfromcarbs}")

#6There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10. Write a program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales

class_a = 20
class_b = 15
class_c = 10
tickets_a = float(input("How many Class A tickets seats were sold"))
tickets_b = float(input("How many Class B tickets seats were sold"))
tickets_c = float(input("How many Class C tickets seats were sold"))
total_income = (class_a * tickets_a) + (class_b * tickets_b) + (class_c * tickets_c)
print(f"Total amount made is: {total_income}")

#9

feet = float(input("Enter a number of feet: "))
feet_to_inches = feet * 12
print(f"there is {feet_to_inches} inches in {feet}ft")

#10

def math_quiz():
    try:
        num1 = random.randint(1, 999)
        num2 = random.randint(1, 999)

        # Display the quiz question
        print(f"What is {num1} + {num2}?")

        # Get user input and validate
        user_input = input("Your answer: ").strip()
        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            return

        user_answer = int(user_input)
        correct_answer = num1 + num2

        # Check the answer
        if user_answer == correct_answer:
            print("🎉 Congratulations! That's correct.")
        else:
            print(f"❌ Incorrect. The correct answer is {correct_answer}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

math_quiz()
#11
tests = int(input("How many tests? "))
while tests <= 0:
    print("Please enter at least one test.")
    tests = int(input("How many tests? "))

total_score = 0.0
for test_number in range(1, tests + 1):
    test_score = float(input(f"Enter test {test_number} score: "))
    total_score += test_score

calc_average = total_score / tests
print(f"Average score: {calc_average:.2f}")

if calc_average >=100:
    grade = "A+"
elif calc_average >= 90:
    grade = "A"
elif calc_average >= 80:
    grade = "B"
elif calc_average >= 70:
    grade = "C"
elif calc_average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")