n = int(input())
arr = list(map(int, input().split()))
m = int(input())

for i in range(n):
	for j in range(i+1,m):
		print(sum(arr[i:j]))