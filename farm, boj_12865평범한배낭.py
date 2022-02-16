n, k = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*w for _ in range(n)]

for i in range(n):
    for j in range(k):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[n-1][k-1])