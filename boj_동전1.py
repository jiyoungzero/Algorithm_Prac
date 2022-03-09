import sys
n, k = map(int, input().split())
# 동적계획법 사용
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
coins.sort()
#  10 --> 1, 2, 5
# 모든 코인을 사용
for coin in coins:


print(cnt)

