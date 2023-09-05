class Solution:
    def count(self, coins, N, Sum):
        a = [[0] * (Sum + 1) for _ in range(N + 1)]
    
    # Initialize the first row.
        for j in range(Sum + 1):
            a[0][j] = 1 if j == 0 else 0
    
        for i in range(1, N + 1):
            for j in range(Sum + 1):
                if coins[i - 1] > j:
                    a[i][j] = a[i - 1][j]
                else:
                    a[i][j] = a[i - 1][j] + a[i][j - coins[i - 1]]
    
        return a[N][Sum]


                
                    
        # code here 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))
        
#https://practice.geeksforgeeks.org/problems/coin-change2448/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article