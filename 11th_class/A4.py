# Check whether a given Text is Palindrome or not
def isPlalindrome(text):
    i = 0
    j = len(text) - 1
    result = True
    while(j > i):
        if(text[i] != text[j]):
            result = False
            break
        j -= 1
        i += 1
    return result

text = str(input("Enter the text for checking : "))
print(isPlalindrome(text))