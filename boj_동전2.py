import sys
x, n = map(int, input().split())
coins = list(map(int ,sys.stdin.readline().split()))
coins.sort(reverse=True)
dp = [1000001]*(n+1) # 동전의 개수를 나타내는 배열
dp[0] = 0

for coin in coins:
	for i in range(coin, n+1):
		dp[i] = min(dp[i], dp[i-coin]+1)
if dp[n] == 1000001:print(-1)
else:print(dp[n])