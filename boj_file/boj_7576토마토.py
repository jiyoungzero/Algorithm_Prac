from collections import deque
import sys

# 입력 받을 때 아예 반대로 받기 > 나중에 x, y 좌표 편하게 하기 위해
n, m = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
queue = deque([])


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if nx < 0 or ny < 0 or nx >= n or ny > m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] += 1
                queue.append([nx, ny])


ans = -10
bfs()
for row in graph:
    for ele in row:
        if ele == 0:
            print(-1)
            exit(0)
        ans = max(ans, ele)
print(ans)
