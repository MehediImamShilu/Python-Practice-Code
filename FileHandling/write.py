# NOTE: This .py code tries to retrieve the demo2.txt file
# writing a file

f = open("D:\Practices\Python\PythonCode\FileHandling\demo2.txt", "a")
f.write("This file now has a line.")
f.close()

# open & read the file after appending
f = open("D:\Practices\Python\PythonCode\FileHandling\demo2.txt", "r")
print(f.read())
