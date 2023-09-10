input = [1,2,3,4,5]
input.sort()
sums = 0
for i in range(len(input)-1):
    sums += abs(input[i]- input[i+1])
print(sums)