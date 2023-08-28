#Find the number of occurence of a character in a string
myString = "aaannjitha"
charCount = {}
for char in myString:
    if char in charCount:
        charCount[char] += 1
    else:
        charCount[char] = 1
for char,count in charCount.items():
    print(char + " Occurs " + str(count) + " times ")
    
