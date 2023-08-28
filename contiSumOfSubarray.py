#A sum will be given, sum of continous elements in the array will give the sum,
# the indexes of leftmost and rightmost needs to be printed
class Solution:
    def subArraySum(self,arr, n, sum_):
        A = []
        current_sum = arr[0]
        start = 0
        i = 1
        while i<=n:
            while(current_sum>sum_ and start< i-1):
                current_sum -= arr[start]
                start += 1
            if(current_sum==sum_):
                A.append(start+1)
                A.append(i)
                return A
            if(i<n):
                current_sum += arr[i]
            i+=1
        A.append(-1)
        return A
solution = Solution()
n = int(input("Plz enter the number of elements :"))
s = int(input("Plz enter the sum :"))
arr = []
for i in range(n):
    element = int(input(f"Plz enter element {i+1} :"))
    arr.append(element)
IndexesAre = solution.subArraySum(arr,n,s)
print(IndexesAre)