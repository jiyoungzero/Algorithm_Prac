n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
mod = 10**9+7
dp = [[0 for _ in range(2000)] for _ in range(2000)]
for i in range(n):
	for j in range(n):
		if arr[i][j] == '.':arr[i][j] = 0
		else:arr[i][j] = 1

if arr[0][0] == 0:dp[0][0] = 1
for i in range(1, n):
	for j in range(1, n):
		if i==0 and j==0 : continue
		if arr[i][j] == 1:continue
		dp[i][j] = dp[i][j-1] + dp[i-1][j]
		dp[i][j] %= mod
print(dp[n-1][n-1])