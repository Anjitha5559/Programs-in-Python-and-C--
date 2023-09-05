class Solution:
    def minCoins(self, coins, M, V):
        a = [[0] * (V + 1) for _ in range(M + 1)]
        
        for j in range(V + 1):
            a[0][j] = float('inf')  # Initialize to infinity, representing we cannot make change initially.

        for i in range(1, M + 1):
            for j in range(1, V + 1):
                if coins[i-1] > j:
                    a[i][j] = a[i - 1][j]
                else:
                    a[i][j] = min(a[i - 1][j], 1 + a[i][j - coins[i-1]])

        if a[M][V] == float('inf'):
            return -1
        else:
            return a[M][V]

	    
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		v,m = input().split()
		v,m = int(v), int(m)
		coins = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minCoins(coins,m,v)
		print(ans)
#https://practice.geeksforgeeks.org/problems/number-of-coins1824/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article