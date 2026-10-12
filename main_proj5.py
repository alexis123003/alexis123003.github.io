#Write a program that gives simple math quizzes. The program should display two random numbers that are to be added, subtracted, multiplied or divided, such as:
#Directions
#The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be displayed. If the answer is incorrect, a message showing the correct answer should be displayed.

#When the student types "done" the program will output The number of questions answered, number of correct answers, number of incorrect answers, and their grade correct/total.

#Create functions for the following:

#Generating a random math problem print it, and return the correct answer.
#For division problems only generate random numbers that divide into whole numbers. 


from random import randint, choice


def generate_math_problem():
    num1 = randint(1, 999)
    num2 = randint(1, 999)
    operation = choice(['+', '-', '*', '/'])

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        num2 = randint(1, 999)
        num1 = num2 * randint(1, 999 // num2)
        correct_answer = num1 // num2

    print(f"What is {num1} {operation} {num2}?")
    return correct_answer


def main():
    total_questions = 0
    correct_questions = 0

    while True:
        correct_answer = generate_math_problem()

        while True:
            user_answer = input("Your answer (or 'done' to finish): ").strip()
            if user_answer.lower() == 'done':
                incorrect_questions = total_questions - correct_questions
                grade = correct_questions / total_questions * 100 if total_questions else 0
                print(f"Questions answered: {total_questions}")
                print(f"Correct answers: {correct_questions}")
                print(f"Incorrect answers: {incorrect_questions}")
                print(f"Grade: {correct_questions}/{total_questions} ({grade:.1f}%)")
                return

            try:
                answer = int(user_answer)
            except ValueError:
                print("Please enter a whole number or 'done'.")
                continue

            total_questions += 1
            if answer == correct_answer:
                correct_questions += 1
                print("That's correct.")
            else:
                print(f"Sorry, the correct answer is {correct_answer}.")
            break


if __name__ == "__main__":
    main()
