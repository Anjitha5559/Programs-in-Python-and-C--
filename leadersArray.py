class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        myVector = []
        r = A[N-1]
        for i in range(N-2, -1, -1):  # Iterate in reverse from N-2 to 0
            if A[i] > r:
                r = A[i]
                myVector.insert(0,A[i])
        
        myVector.append(A[N-1])
        return myVector
