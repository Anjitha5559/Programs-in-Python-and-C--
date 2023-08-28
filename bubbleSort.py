def bubbleSort(arr,n):
    for i in range(len(arr)):
        for j in range(i+1):
            if(arr[j]>arr[i]):
                arr[j],arr[i] = arr[i],arr[j]
    return arr
        

n = int(input("Plz enter the number of terms :"))
arr = []
for i in range(n):
    element = int(input(f"Plz enter element {i+1} :"))
    arr.append(element)
arr = bubbleSort(arr,n)
print(arr)
