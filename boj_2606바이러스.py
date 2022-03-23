import sys
from collections import deque

n = int(input())
pair = int(input())
ans = 0
graph = [[] for _ in range(n+1)]
visited = [False] * n

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    global ans
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                ans += 1
    return ans


print(bfs(1))
