n, m = tuple(map(int, input().split()))

visited = [False]*(n+1)
arr = [0]*m

def dfs(x):
	if x == m:
		for i in range(m):
			print(arr[i], end=" ")
		print()
		return
	for i in range(1, n+1):
		if not visited[i]:
			arr[x] = i			
			visited[i] = True
			dfs(x+1)
			visited[i] = False
			
dfs(0)			
			