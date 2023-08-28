#number of digits in a string
myString = "Anjitha970001"
num = 0
for i in range(len(myString)):
    if(myString[i] in "0123456789"):
        num = num + 1
print(num)   