with open("myfile.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("\nNew text")
    # print(file.read())