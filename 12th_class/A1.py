# Recursively find the factorial of a natural number.

x = int(input("Enter a number :"))
factorial = 1
for i in range(x,0,-1):
    factorial *= i
print('factorial of ' + str(x) + ' is ' + str(factorial))