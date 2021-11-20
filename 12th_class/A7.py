# Write a recursive code to compute the n
# th Fibonacci number

a = 0
b = 1
sum = 0
no_of_times = 15

while(no_of_times >0):
    print(a, end=", ")
    sum = a + b
    a = b
    b = sum
    no_of_times-=1