n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
l,r = 0, max(arr)

def check(x):
	s_len = 0
	for i in range(n):
		if arr[i] >= x:
			s_len += arr[i]-x
	return s_len

while l<=r:
	mid = (l+r)//2
	if check(mid) >= m: l = mid+1
	else: r = mid-1
		
print(r)