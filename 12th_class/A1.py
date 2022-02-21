# Recursively find the factorial of a natural number.

x = int(input("Enter a number :"))
def gcd(a,b):
    if(b ==0):
        return a
    else:
        return gcd(b,a % b)
print(gcd(4,12))
    
    
       
