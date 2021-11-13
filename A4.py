# Check whether a given Text is Palindrome or not

def easy(value):
    if (value == value[::-1]):
        print("Is palindrome")
    else:
        print("Not Palindrome")

def hard(value):
    list = []
    for a in value:
        list.append(a)
    list.reverse()
    revlist = list
    revText = ""
    for a in revlist:
        revText += a
    if(value == revText):
        print("Is palindrome")
    else:
        print("Not Palindrome")


text = str(input("Enter the text for checking : "))
easy(text)