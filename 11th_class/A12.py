# Create a dictionary with the roll number, name and marks of n 
# students in a class and display the
# names of students who have scored marks above 75.

dict = {1:["Surya",45],
        2:["Sultan",55],
        3:["Swaroop",85],
        4:["Prativa",82],
        5:["Tapaswinee",78],
        6:["Sekhar",35],
        7:["Sayeda",99],
        8:["Priyanka",76],}
for item in dict.values():
    if(item[1] > 75):
        print(item[0])
