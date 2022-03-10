import sys
n, k = map(int, input().split())
# 동적계획법 사용
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1  # 동전이 1개일 경우
#  10 --> 1, 2, 5
# 모든 코인을 사용
for coin in coins:
    for i in range(coin, k+1):
        if i-coin >= 0:
            dp[i] += dp[i-coin]
print(dp[k])
