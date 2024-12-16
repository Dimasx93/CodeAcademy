# Exercise 1: Reading and Writing a Simple Text File (Beginner)

# with open("data.txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     print(line)
#
# with open("data.txt", "a") as f:
#     lines = f.write("\nStefano, 31\n")
#
# with open("data.txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     print(line)

# Exercise 2: Counting Words in a File (Intermediate)

# tot_words = 0
# tot_python = 0
#
# with open("sample.txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     # print(line)
#     line = line.strip()
#     # Count occurrences of the word "python" (case-insensitive)
#     new_python_count = line.lower().count("python")
#     tot_python += new_python_count
#
#     # Count characters excluding spaces
#     text_without_spaces = line.replace(" ", "")  # Remove spaces
#     new_count = len(text_without_spaces)  # Count remaining characters
#     tot_words += new_count
#
# # Output the results
# print(f"Total characters excluding spaces: {tot_words}")
# print(f"Total occurrences of 'python': {tot_python}")

#Exercise n3 Log File Analysis

# with open("error.log", "x"):
#     pass
with open("error.log" , "a") as x:

    with open("server.log", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            if "ERROR" in line:
                x.write(line)


info_count = 0
error_count = 0

with open("server.log" , "r") as f:
    lines = f.readlines()
    for line in lines:
        info_count += line.lower().count("info")
        error_count += line.lower().count("error")
    print(f"INFO entries: {info_count}")
    print(f"ERROR entries: {error_count}")