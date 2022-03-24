# (다이나믹프로그래밍)
import sys
# 일단 코인을 입력 받고 sorted(오름차순으로)한다. 
# dp 배열 k+1만큼 만들어서 1로 더했을 때의 최대 10001를 담을 수 있게끔 해준다. 
# dp 배열의 초기값(아무겂도 안더해줬을 때)는 0개,
# 코인을 더해 줄 때 그 다음 코인을 더해주는 것과 
# dp[price] = 개수
# 현재의 개수에 새로운 코인을 더했을 경우,
# 현재의 개수로만 조합했을 경우,   

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
sorted(coins)
dp = [10001] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1 )

if dp[k] != 10001:
    print(dp[k])
else:
    print(-1)






