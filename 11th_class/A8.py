
# Test if a number is equal to the sum of the cubes of its digits.


number = int(input("Enter the value : "))
# Get the digits in to a list
list =[]
sum = 0
for i in str(number):
    list.append(int(i))
    
for i in list:
    sum += (i ** 3)

if(number == sum):
    print("Yes it is")
else:
    print("No")