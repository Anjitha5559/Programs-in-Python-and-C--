class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        a = [[0]* (W+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,W+1):
                if i==0 or j == 0:
                    a[i][j] = 0
                elif wt[i-1] <= j:
                    a[i][j] = max(a[i-1][j],a[i-1][j-wt[i-1]]+val[i-1])
                else:
                    a[i][j] = a[i-1][j]
        return a[i][j]
        
    # def knapSack(self, W, wt, val, n):
    #     a = [[0] * (W + 1) for _ in range(n + 1)]
    #     for i in range(1, n + 1):
    #         for j in range(1, W + 1):
    #             if i == 0 or j == 0:
    #                 a[i][j] = 0
    #             elif wt[i - 1] <= j:
    #                 a[i][j] = max(a[i - 1][j], val[i - 1] + a[i - 1][j - wt[i - 1]])
    #             else:
    #                 a[i][j] = a[i - 1][j]
    #     return a[n][W]


            
            
        
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
#https://www.youtube.com/watch?v=PfkBS9qIMRE&list=PLdo5W4Nhv31aBrJE1WS4MR9LRfbmZrAQu&index=5