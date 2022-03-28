import sys
from collections import deque

r = sys.stdin.readline()
n = int(r)
ans = 0
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
graph = [list(map(int, r)) for _ in range(n)]
visited = [[0]*(n+1) for _ in range(n+1)]

def bfs(x,y):
    global ans
    queue = deque([])
    queue.append([x,y])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft([])
        for i in range(4):
            nx, ny = x+dxs[i], y+dys[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                queue.append([nx,ny])
                visited[nx][ny] += 1
    ans += 1 

bfs(0,0)
print(ans)
