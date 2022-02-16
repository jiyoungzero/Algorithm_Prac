import sys
sys.setrecursionlimit(6000000)
n = int(input())
dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
arr = [map(int, sys.stdin.readline().split()) for _ in range(n)]

for i in range(1,n+1):
    a, b, c = arr[i-1][0], arr[i-1][1], arr[i-1][2]
    dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + a
    dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + b
    dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + c
    
print(max(dp[n]))