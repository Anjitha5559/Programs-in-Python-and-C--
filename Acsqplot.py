input = [64,16,38,81,50,100]
output = []
for i in range(len(input)):
    val = int(input[i]**.5)
    if input[i] > 0 and input[i] == val * val:
        output.append(input[i])
    else:
        False
print(output)
print(len(output))