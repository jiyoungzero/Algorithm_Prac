n, q = tuple(map(int,input().split()))
pos = list(map(int, input().split()))
def low_search(pos, a):
	low, high = 0, n
	while low<high:
		mid = (low+high)//2
		if pos[mid] < a:
			low = mid+1
		else:
			high = mid
	return low
	
def high_search(pos, a):
	low, high = 0, n
	while low<=high:
		mid = (low+high)//2
		if pos[mid] <= a:
			low = mid+1
		else:
			high = mid
	return high
	
for i in range(n):
	pos.sort() # 오름차순 정렬

for i in range(q):
	a, b = tuple(map(int, input().split()))
	low = low_search(pos, a)
	high = high_search(pos, b)
	print(high-low)