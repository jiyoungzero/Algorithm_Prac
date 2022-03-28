from collections import deque

n = int(input())
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*(n+1) for _ in range(n+1)]
count = []


def bfs(x, y):
    global count
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        cnt = 0
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dxs[i], y+dys[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == True:
                queue.append([nx, ny])
                visited[nx][ny] = True
                cnt += 1
    count.append[cnt]
    return count


bfs(0, 0)
print(len(count))
