sales = []

for day in range(1, 8):
    while True:
        try:
            daily_sales = float(input(f"Enter sales for day {day}: "))
            sales.append(daily_sales)
            break
        except ValueError:
            print("Please enter a valid sales amount.")

total_sales = sum(sales)
print(f"Total sales for the week: ${total_sales:,.2f}")

input("Press Enter to continue to the next section...")

values = []

for count in range(1, 21):
    while True:
        try:
            number = float(input(f"Enter number {count}: "))
            values.append(number)
            break
        except ValueError:
            print("Please enter a valid number.")

lowest = min(values)
highest = max(values)
total = sum(values)
average = total / len(values)

print(f"Lowest number: {lowest}")
print(f"Highest number: {highest}")
print(f"Total of the numbers: {total}")
print(f"Average of the numbers: {average}")

input("Press Enter to continue to the next section...")

correct_answers = [
    "A", "C", "A", "A", "D",
    "B", "C", "A", "C", "B",
    "A", "D", "C", "A", "D",
    "C", "B", "B", "D", "A"
]

with open("unit_7_7.txt", "r") as file:
    student_answers = [line.strip().upper() for line in file if line.strip()]

correct_count = 0
incorrect_questions = []

for index in range(len(correct_answers)):
    if index < len(student_answers) and student_answers[index] == correct_answers[index]:
        correct_count += 1
    else:
        incorrect_questions.append(index + 1)

passed = correct_count >= 15

print(f"Passed: {passed}")
print(f"Correct answers: {correct_count}")
print(f"Incorrect answers: {20 - correct_count}")
print(f"Incorrect question: {incorrect_questions}")

input("Press Enter to continue to the next section...")

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def display_primes(label, numbers):
    print(f"{label}:")
    for number in numbers:
        if is_prime(number):
            print(number)


def main():
    while True:
        try:
            limit = int(input("Enter an integer greater than 1: "))
            if limit > 1:
                break
            print("Please enter a number greater than 1.")
        except ValueError:
            print("Please enter a valid integer.")

    numbers = list(range(2, limit + 1))
    display_primes("prime number(s)", numbers)


if __name__ == "__main__":
    main()



