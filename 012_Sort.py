#Dutch National Flag ALgorithm

def dutchNationalFlag(arr,n):
    low=0
    mid = 0
    high = n-1
    while (mid<=high):
        if(arr[mid]==0):
            arr[mid],arr[low] = arr[low],arr[mid]
            mid+=1
            low+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
    return arr
n = int(input("Plz enter the number of elements in the array :"))
arr = []
for i in range(n):
    elements = int(input("Plz enter 0's 1's and 2's to sort out :"))
    arr.append(elements)
sorted_out = dutchNationalFlag(arr,n)
print(sorted_out)
    
    
