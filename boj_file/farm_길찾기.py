n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
mod = 10**9+7
dp = [[0 for _ in range(2000)] for _ in range(2000)]
for i in range(n):
	for j in range(n):
		if arr[i][j] == '.':arr[i][j] = 0
		else:arr[i][j] = 1

if arr[0][0] == 0:dp[0][0] = 1 # 맨 처음에 갈때는 경우의 수가 0 (벽인 경우는 제외)
for i in range(n):
	for j in range(n):
		# 모든 arr를 돌면서 벽이면 통과
		if arr[i][j] == 1:continue
		if i==0 and j==0 : continue # 이미 위에서 정의
		dp[i][j] = dp[i][j-1] + dp[i-1][j]
		dp[i][j] %= mod
print(dp[n-1][n-1])
	