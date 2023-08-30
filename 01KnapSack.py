n = int(input("Plz Enter the Number of Objects :"))
W = int(input("Plz Enter the weight of the sack"))
arr = []
for i in range(n):
    elements = int(input("Plz Enter the elements"))
    arr.append(elements)
def knapSack(W,wt,n,val):
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n):
        for w in range(1,w):
            if wt[i-1]<=W:
                dp[n][w] = max(val(i-1)+ dp[i-1][w-wt[i]],dp[i-1][w])
            else:
                dp[n][w]  =dp[i-1][w]
    return dp[n][w]
dp = knapSack(W,wt,n,val)

        
    