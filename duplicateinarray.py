def duplicates(arr, n):
    arr.sort()
    A = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            A.append(arr[i])
    if len(A) == 0:
        A.append(-1)
        return A
    else:
        A = list(set(A))
        A.sort()
        return A

n = int(input("Please enter the number of terms: "))
arr = []
for i in range(n):
    element = int(input(f"Please enter element {i+1}: "))
    arr.append(element)

soln = duplicates(arr, n)
print(soln)
