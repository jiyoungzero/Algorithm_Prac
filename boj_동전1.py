import sys
n, k = map(int, input().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]
ans = 0
coins.sort(reverse=True)

# 큰 수 부터 나누고 더이상 나눠지지 않으면 그 다음으로 큰 수
for coin in coins:
    if k == 0:break
    ans += (k//coin)
    k %= coin
print(ans)