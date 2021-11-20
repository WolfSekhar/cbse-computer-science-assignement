# Write a Python function sin(x, n) to calculate the value of sin(x) using its Taylor series 
# expansion up to n terms. Compare the values of sin(x) for different values of n with the correct 
# value.

import math

def factorial(number):
    fact = 1
    for i in range(number,0,-1):
        fact *= i
    return fact

def degree_to_rad(degree):
    return degree * (math.pi / 180)

def sin(x,n):
    x = degree_to_rad(x)
    sum = 0
    for i in range(n):
        a = (-1) ** i
        b = factorial((2 * i) + 1)
        c = x ** ((2 * i) + 1)
        sum = sum + ((a * c) / b)
    return sum

print(sin(45,30))

#    Uncomment to see the difference between Tylor's series
#    and math library obtained sine values
#
# for d in range(90):
#     print("Obtained Val : ",sin(d,40))
#     print("Actual Val : " ,math.sin(degree_to_rad(d)))
#     print("***********************************")