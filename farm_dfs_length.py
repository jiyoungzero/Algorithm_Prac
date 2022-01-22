N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] # 건초더미 좌표 리스트
graph = [[0]*(N+1) for _ in range(N+1) ] # 전체 맵
visited = [[False]*102 for _ in range(102)]
cnt = 0
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

for i in range(N):
	a, b = arr[i][0], arr[i][1]
	if graph[a][b] == 0: # 건초더미 위치 = 1
		graph[a][b] = 1
	else:continue
		
def dfs(x, y):
	visited[x][y] = True
	for i in range(4):
		nx = x + dxs[i]
		ny = y + dys[i]
		if nx < 0 or nx > 101 or ny < 0 or ny > 101:
			continue
		elif visited[nx][ny] == False and graph[nx][ny] == 0:
			dfs(nx, ny)
			
dfs(0,0)
			
for i in range(N+1):
	for j in range(N+1):
		if graph[i][j] == 1:
			for k in range(4):
				nx = x + dxs[i]
				ny = y + dys[i]
				if graph[nx][ny] == 0 and visited[nx][ny] == True:
					cnt += 1
		
print(cnt)		
		