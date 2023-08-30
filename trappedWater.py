def trapped_water(arr,n):
    left_max = [0]*n
    right_max = [0]*n
    left_max[0] = arr[0]
    right_max[n-1] = arr[n-1]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1],arr[i])
    for i in range(n-2,-1,-1):
        right_max[i] = max(right_max[i+1],arr[i])
    trapped_Water = 0
    for i in range(n):        
        trapped_Water += min(left_max[i],right_max[i]) - arr[i]
    return trapped_Water
n = int(input("Plz Enter the number of elements :"))
arr = []
for i in range(n):
    element = int(input(f"Plz Enter the element {i+1} :"))
    arr.append(element)
trapped_Water = trapped_water(arr,n)
print(trapped_Water)
      
    