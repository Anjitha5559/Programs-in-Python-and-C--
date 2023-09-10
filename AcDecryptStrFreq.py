myString = "a3b1c2"
alpha = myString[0::2]
num = myString[1::2]
result = ''
print(alpha)
print(num)
charCount = {}
num = list(num)
print(num)
for char, count in zip(alpha, num):
    charCount[char] = int(count)

print(charCount)

for char, count in charCount.items():
    result += (char * count)
print(result)


