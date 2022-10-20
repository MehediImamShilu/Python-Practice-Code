# To delete a file, you have to use OS module
# os.remove() method

import os

# check if file exist, the delete
if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("The file doesn't exist!")

# To remove a folder
# after importinf os module

# os.rmdir("myFolder")
