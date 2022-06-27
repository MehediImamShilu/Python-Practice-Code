score = input("Enter score: ")

try:
    s = float(score)
except:
    print("Enter a numeric value.")
    quit()

if s > 1.0:
    finalPoint = "Point is out of range."
elif s >= 0.9:
    finalPoint = "A"
elif s >= 0.8:
    finalPoint = "B"
elif s >= 0.7:
    finalPoint = "C"
elif s >= 0.6:
    finalPoint = "D"
elif s < 0.6:
    finalPoint = "F"
else:
    finalPoint = "Error!"
print(finalPoint)
