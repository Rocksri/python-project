with open("hello.txt", "w") as file:
    lines = ["Hello ", "World"]
    file.writelines(lines)
