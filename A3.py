# Check if a number is prime or not

number = int(input("Enter the Number: "))
check = True
for i in range(2,(number // 2) + 1):
    if (number % i == 0):
        check = False
        break
if(check):
    print("The number is prime")
else:
    print("The number is not prime")