# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
hrs = input("Enter Hours: ")
rate = input("Enter rate: ")

# checks the type of value; ex- numeric or string
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Please, enter numeric value.")
    quit()
print(h, r)

# checking the condition
if h <= 40:
    pay = (h * r)
else:
    pay = (40 * r + (h - 40) * 1.5 * r)
print("Pay:", pay)
