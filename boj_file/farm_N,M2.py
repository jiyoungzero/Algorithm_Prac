n, m = tuple(map(int, input().split()))

visited = [False]*(n+1)
arr = [0]*m

def dfs(x):
	if x == m :
		for i in range(m):
			print(arr[i], end=" ")
		print()
		return
	for i in range(1, n+1):
		if not visited[i] :
			arr[x] = i
			# 숫자 i 이하는 오름차순을 위해 방문처리함
			for j in range(1,i+1):visited[j] = True
			dfs(x+1)
			for k in range(1, i+1):visited[k] = False # 백트래킹
			
dfs(0)			