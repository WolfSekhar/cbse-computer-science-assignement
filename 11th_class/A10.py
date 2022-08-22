# Input a list/tuple of elements, search for a 
# given element in the list/tuple.
L = input("Enter all the elemets with spaces : ")
list = L.split()
searchItem = input("Enter item you want to search : ")

for element in list:
    if(element == searchItem):
        print("Element is availabe")
# if element is not availabe then nothing will be displayed