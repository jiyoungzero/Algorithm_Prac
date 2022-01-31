import sys
sys.setrecursionlimit(1000000)

m,n = tuple(map(int, input().split()))
graph = [list(map(int, input())) for _ in range(m)]
dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def dfs(x, y):
	global dxs, dys
	graph[x][y] = 2 # 방문함
	for i in range(4):
		nx = x + dxs[i]
		ny = y + dys[i]
		if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
			dfs(nx,ny)
for i in range(n):
	dfs(0,i)
if graph[-1].count(2) > 0:print("YES")
else: print("NO")