#Sum of all the sub arrays of the array with k = 3
array = [2,3,1,4,7,6,5]
maxSum = 0
summ = 0
for i in range(len(array)-3):
    print(i)
    for j in range(i,i+3):
        summ += array[j]
        print(summ)
    maxSum = max(maxSum,summ)
    summ = 0
print(maxSum)


# left = 0
# for right in range(2,len(array)):
#     summ = array[left]+array[right]+array[left+1]
#     maxSum = max(maxSum,summ)
# print(maxSum)
    
    