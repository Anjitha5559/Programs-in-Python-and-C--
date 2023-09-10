input = [1,0,2,3,0,0,0,4,5,6]
for i in range(len(input)-1):
    for j in range(len(input)-1):
        if input[j] == 0:
         input[j], input[j+1] = input[j+1], input[j]      
print(input)