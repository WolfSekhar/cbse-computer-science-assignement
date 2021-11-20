# Write a recursive Python program to test if a string is a palindrome or not.

def isPalindromeEasy(value):
    if (value == value[::-1]):
        print("Is palindrome")
    else:
        print("Not Palindrome")

def isPalindrome(value):
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
isPalindrome(text)