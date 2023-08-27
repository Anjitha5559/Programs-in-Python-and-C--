class Solution:
    def missingNumber(self, array, n):
        sum0 = n * (n + 1) // 2
        sum1 = 0 
        for i in range(n):
            sum1 = sum1 + array[i]
        missing = sum0 - sum1
        return missing

# Get the number of terms as input
n = int(input("Please enter the number of terms: "))

# Initialize an empty list to store the numbers
myarray = []

# Get the numbers from the user
for i in range(n):
    number = int(input("Please enter a number: "))
    myarray.append(number)

# Create an instance of the Solution class
solution = Solution()

# Call the missingNumber method and store the result
missing = solution.missingNumber(myarray, n)

# Print the missing number
print("The missing number is:", missing)
