#This is done using Kadane's Algorithm
def maximumSum(arr,n):
    curSum = 0
    maxSub = arr[0]
    for n in arr:
        if curSum<0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub,curSum)
    return maxSub
    # current_sum = arr[0]
    # maximum_sum = arr[0]
    # for i in range(1,n):
    #     current_sum = max(arr[i],current_sum+arr[i])
    #     maximum_sum = max(current_sum,maximum_sum)
    # return maximum_sum
n = int(input("Plz enter the number of terms :"))
arr = []
for i in range(n):
    element = int(input(f"Plz enter element {i+1} :"))
    arr.append(element)

A = maximumSum(arr,n)
print(A)