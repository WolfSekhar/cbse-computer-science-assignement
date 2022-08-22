# Input a list of numbers and swap elements at the even 
# location with the elements at the odd location.

# list with total even number of items are allowed
print("ONLY ENTER EVEN NUMBER OF NUMBERS")
L = input("Enter all the number with spaces : ")
list = L.split()

def method1():
    for i in range(0,len(list),2):
        list[i],list[i + 1] = int(list[i + 1]), int(list[i])
    print(list)
# Swap using variable
def method2():
    for i in range(0,len(list),2):
        a = list[i]
        b = list[i + 1]
        list[i] = b
        list[i + 1] = a
    print(list)

method1()