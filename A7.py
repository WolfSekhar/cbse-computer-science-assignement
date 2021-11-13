# LCM of two numbers
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
LCM = 1
while(LCM >=1):
    if(LCM % a == 0 and LCM % b == 0):
        break
    LCM +=1
print(LCM)