import sys

if len(sys.argv) == 1:
    print("USEAGE: python commandline.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
