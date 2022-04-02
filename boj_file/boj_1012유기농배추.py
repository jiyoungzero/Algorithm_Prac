# bfs
from collections import deque
from glob import glob
import sys

n = int(input())
w, h, k = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
visited = [[False]*(w+1) for _ in range(h+1)]
cnt = 0
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
count = []


def bfs(x, y):
    global cnt
    queue = deque()
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dxs[i], y+dys[I]
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


for i in range(h):
    for j in range(w):
        if not visited[i][j] and graph[i][j] == 1:
            count.append(bfs(i, j))
print(len(count))
