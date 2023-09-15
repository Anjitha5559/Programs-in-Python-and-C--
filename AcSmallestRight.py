input = [3,2,11,7,6,5,6,1]
for i in range(len(input)):
    for j in range(i,len(input)):
        
        if input[j] < input[i]:
            input[i], input[j] = input[j],input[i]
            break
input[len(input)-1] = -1
print(input)
#remaining is pending
        