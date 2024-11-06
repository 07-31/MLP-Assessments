
with open("my_file.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Here is the second line with a number: 12345\n")
    file.write("Finally, the third line with some more text and numbers: 67890\n")


with open("my_file.txt", "r") as file:
    content = file.read()
    print("Contents of 'my_file.txt' after initial write:")
    print(content)


with open("my_file.txt", "a") as file:
    file.write("This is an appended fourth line.\n")
    file.write("Adding a fifth line with more information.\n")
    file.write("And here's a sixth line to finish off the file.\n")


with open("my_file.txt", "r") as file:
    updated_content = file.read()
    print("\nContents of 'my_file.txt' after appending additional lines:")
    print(updated_content)
