def print2largest(arr, n):
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    if len(arr) < 2:
        return -1
    else:
        return arr[-2]

n = int(input("Please enter the number of terms: "))
arr = []
for i in range(n):
    element = int(input(f"Please enter element {i+1}: "))
    arr.append(element)

soln = print2largest(arr, n)
print(soln)
