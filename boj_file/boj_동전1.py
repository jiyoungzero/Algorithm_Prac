import sys
n, k = map(int, input().split())
# 동적계획법 사용
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1  # 동전이 1개일 경우

#     1 2 3 4 5 6 7 8 9 10
# 1 /  1 1 1 1 1 1 1 1 1  1
# 2 / 0 1 1 2 2 3 3 4 4  5
# 5 /  0 0 0 0 1 1 2 2 3  4
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
print(dp[k])
