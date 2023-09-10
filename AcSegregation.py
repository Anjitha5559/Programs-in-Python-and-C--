input = list(range(1,20,1))
output = []
for i in range(len(input)):
    if input[i] % 2 == 0:
        output.append(input[i])        
print(input)
for i in range(len(input)):
    if input[i] %2 != 0:
        output.append(input[i])
print(output)
    