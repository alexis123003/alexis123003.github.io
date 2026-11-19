# Write a program that creates a dictionary containing course numbers and
# the room numbers of the rooms where the courses meet.
#
# Course Number (key)    Room Number (value)
# CS101    3004
# CS102    4501
# CS103    6755
# NT110    1244
# CM241    1411

courses = {
    "CS101": (3004, "Haynes", "8:00 a.m."),
    "CS102": (4501, "Alvarado", "9:00 a.m."),
    "CS103": (6755, "Rich", "10:00 a.m."),
    "NT110": (1244, "Burke", "11:00 a.m."),
    "CM241": (1411, "Lee", "1:00 p.m.")
}

with open("courses.txt", "w") as file:
    for course, (room, instructor, time) in courses.items():
        file.write(f"Course Number: {course}, Room Number: {room}, Instructor: {instructor}, Meeting Time: {time}\n")
with open("courses.txt", "r") as file:
    print(file.read())
file.close()


# Write a program that uses a dictionary to assign "codes" to each letter of the alphabet.
# For example, A -> %, a -> 1, B -> @, etc.
import string

upper_symbols = "%@#$&*+-/=^~`|{}[]<>?,!;:"
lower_symbols = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:len(string.ascii_lowercase)]

codes = {
    letter: symbol
    for letter, symbol in zip(string.ascii_uppercase, upper_symbols)
}
codes.update({
    letter: symbol
    for letter, symbol in zip(string.ascii_lowercase, lower_symbols)
})

with open("codes.txt", "w", encoding="utf-8") as file:
    for letter, code in codes.items():
        file.write(f"{letter} -> {code}\n")

# Read the course list and apply the code dictionary to each character.
with open("courses.txt", "r", encoding="utf-8") as file:
    course_lines = file.readlines()

encoded_courses = []
for line in course_lines:
    encoded_line = "".join(codes.get(char, char) for char in line)
    encoded_courses.append(encoded_line)

with open("coded_courses.txt", "w", encoding="utf-8") as file:
    file.write("".join(encoded_courses))
file.close()

with open("coded_courses.txt", "r", encoding="utf-8") as file:
    print(file.read())
