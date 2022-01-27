def dfs(x,y):
    	global dxs, dys
	if x < 0 or x>=m or y<0 or y>=n:
		return False
	if graph[x][y] == 0:
		graph[x][y] = 2 # 방문함
		for i in range(4):
			nx = x + dxs[i]
			ny = y + dys[i]
			dfs(nx, ny)
		return True
	return False

m,n = tuple(map(int, input().split()))
graph = [list(map(int, input())) for _ in range(m)]
dxs = [-1,1,0,0]
dys = [0,0,1,-1]
for i in range(n):
	if graph[0][i] == 0:
		dfs(0,i)
				
if graph[m-1].count(2) > 0:
	print("YES")
else:
	print("NO")