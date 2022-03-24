from collections import deque

n, m = map(int, input().split())
graph = [ list(map(int, input())) for _ in range(n) ]
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
  queue = deque([])
  queue.append([x,y])

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dxs[i]
      ny = y + dys[i]

      if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n-1][m-1]

ans = bfs(0,0)
if ans > 0:print(ans)
else:print(-1)