# using of Loop, conditions & try-except
num = 0
sub_total = 0.0

while True:
    firstInput = input("Enter a number: ")
    # when "done" will be pressed, code will stop it's loop & produce result
    if firstInput == "done":
        break
    # try-except is used for input "int/float" value
    try:
        a = float(firstInput)
    except:
        print("***Invalid Input***")
        continue
    # num = conting the total number is input value
    num = num + 1
    # sub_total = total summing of input value
    sub_total = sub_total + a

averageValue = sub_total / num
print("End", num, sub_total, averageValue)
