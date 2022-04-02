# bfs
from collections import deque
import sys

n = int(input())
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]


def bfs(graph, x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dxs[i], y+dys[i]
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0  # 다음 케이스를 위해 초기화를 미리 해주기
    return


result = []
for _ in range(n):
    w, h, k = map(int, input().split())
    graph = [[0]*(h) for _ in range(w)]
    cnt = 0

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(w):
        for j in range(h):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    result.append(cnt)
for ele in result:
    print(ele)
