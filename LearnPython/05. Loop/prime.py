# for every n from 2 to 10
# for every x from 2 to n
# checking out of remainder of n/x == 0
# if not then it wiil be a prime number

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break

    else:
        print(n, "is a prime number.")
