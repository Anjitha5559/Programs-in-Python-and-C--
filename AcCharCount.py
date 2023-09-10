myString = "annnnnnjitha"
charCount = {}
result = ' '
for char in myString:
    if char in charCount:
        charCount[char]+=1
    else:
        charCount[char] = 1
print(charCount)
for key, value in charCount.items():
    value = str(value)
    result += key + value
print(result)
    