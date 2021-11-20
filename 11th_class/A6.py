# Find the GCD of two integers

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
upValue = b
if a > b:
    upValue = a
for i in range(upValue,0,-1):
    if(a % i == 0 and b % i == 0):
        print("The GCD is " + str(i))
        break