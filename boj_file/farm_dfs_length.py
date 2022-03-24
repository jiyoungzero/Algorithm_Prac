N = int(input())
graph = [[0]*(N+2) for _ in range(N+2) ] # 전체 맵
visited = [[False]*(N+2) for _ in range(N+2)]
cnt = 0
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

for i in range(N):
	a, b = tuple(map(int, input().split()))
	graph[a][b] = 1

def dfs(x, y):
	visited[x][y] = True
	for i in range(4):
		nx = x + dxs[i]
		ny = y + dys[i]
		if nx < 0 or nx > (N+1) or ny < 0 or ny > (N+1):
			continue
		# 아직 방문안했고 건초더미가 없는 곳이면	
		elif visited[nx][ny] == False and graph[nx][ny] == 0:
			dfs(nx, ny)
			
dfs(0,0)
for i in range(N+1):
	for j in range(N+1):
		if graph[i][j] == 1:
			for k in range(4):
				nx = i + dxs[k]
				ny = j + dys[k]
				if graph[nx][ny] == 0 and visited[nx][ny] == True: # 건초더미 주변에 있는 빈곳을 센다(dfs로 방문한 빈곳은 visited로 표현 이걸로 cnt)
					cnt += 1
		
print(cnt)	
		