# This .py code tries to retrieve the demo.txt file

file_handling = open(
    "D:\Practices\Python\PythonCode\FileHandling\demo.txt", "r")

# reading the text file
# print(file_handling.read())

# return first 10 character of the line
# print(file_handling.read(10))

# return the first line
# or return the first two lines
print(file_handling.readline())
print(file_handling.readline())
