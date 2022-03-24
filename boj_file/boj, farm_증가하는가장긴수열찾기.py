import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0 
dp = [0]*n
for i in range(n):
	dp[i] = 1
	for j in range(i):
		if arr[j] < arr[i]: # 이미 for문으로 이전의 모든 작은 수를 탐색할 수 있음 
			dp[i] = max(dp[i], dp[j]+1)
	ans = max(dp[i], ans)
print(ans)