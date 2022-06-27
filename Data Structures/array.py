from array import array

x = array("i", [1, 2, 3])   # python 3 Typecode: "i" is int
# float value can't be used, example
# x[0] = 1.0; is a wrong line
x.append(4)
print(x)
