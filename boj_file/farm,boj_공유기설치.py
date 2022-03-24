n, c = map(int, input().split())
arr = [ int(input()) for _ in range(n)]
arr.sort()
l, r = 0, arr[-1]-arr[0]
def check(x):
	cnt, cur = 1, arr[0]
	for i in range(1,n):
		if cur+x <= arr[i]:
			cur = arr[i]
			cnt += 1
	if cnt >= c: return True
	else:return False
	
while l<r:
	mid = (l+r+1) // 2 #무한루프를 피하기 위해 3,4
	if check(mid) : l=mid
	else: r = mid - 1
print(l)