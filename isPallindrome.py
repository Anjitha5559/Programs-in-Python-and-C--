myString = "nisin"
for i in range(len(myString)):
    if(myString[i]!=myString[len(myString)-i-1]):
        isPalindrome = False
    else:
        isPalindrome = True
if(isPalindrome):
    print(myString+" Is a palindrome")
else:
    print(myString + " Is not a Pallindrome")