with open("main_1.html", "r", encoding="utf-8") as file_2:
    html_content = file_2.read()

name = input("Enter your name: ")
html_content = html_content.replace("{{name}}", name)

about = input("Describe yourself: ")
html_content = html_content.replace("{{about}}", about)

print(html_content)

with open("main_1.html", "w", encoding="utf-8") as file_2:
    file_2.write(html_content)


