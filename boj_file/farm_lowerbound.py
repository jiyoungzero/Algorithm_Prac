import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
k = int(input())
l, r = 1, n 

while l<r:
	mid=(1+n)//2
	if arr[mid] < k:
		l = mid+1
	elif arr[mid] > k:
		r = mid
	else:
		r = mid
		
print(l) # l==r
