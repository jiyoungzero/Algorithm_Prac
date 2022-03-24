# 그래프를 통해 +1 visited 하므로 bfs, dfs 모두 가능
from collections import deque

n = int(input())
n1, n2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)
queue = deque()
def bfs(x):
	queue.append(x)
	while queue:
		f = queue.popleft()
		for i in graph[f]:
			visited[i] += 1
			queue.append(i)
bfs(n1)
print(visited[n2] if visited[n2] > 0 else -1)