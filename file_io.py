with open("input.txt", "r") as file:
    content = file.read()
    print(content)
user_input = input("Enter text to save to file: ")
with open("output.txt", "w") as file:
    file.write(user_input)
with open("output.txt", "a") as file:
    file.write("\nHello, World!")