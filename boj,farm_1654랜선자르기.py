# 이분탐색, l,r 
import sys
n, m = map(int, input().split())
arr = [ int(sys.stdin.readline()) for _ in range(n)]
l, r = 1, max(arr)

while l <= r:
	mid = (l+r) // 2
	ans = 0 # 케이블 개수
	for i in arr:
		ans += i//mid
	if ans >= m : # 목표한 값보다 같거나 많으면
		l = mid+1
	else:
		r = mid - 1
print(l-1)