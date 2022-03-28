from collections import deque

n = int(input())
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*(n+1) for _ in range(n+1)]
count = []


def bfs(x, y):
    global count
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dxs[i], y+dys[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            count.append(bfs(i, j))
count.sort()
print(len(count))
for c in count:
    print(c)
