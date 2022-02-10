import sys
from collections import deque

n,m,s = tuple(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m):
	a, b = tuple(map(int, sys.stdin.readline().split()))
	graph[a].append(b)
	graph[b].append(a)

#작은 것을 먼저 방문하도록
for i in range(n+1):
	graph[i].sort()

def dfs(x):
	global visited, graph
	visited[x] = True
	print(x, end= ' ')
	for ele in graph[x]:
		if not visited[ele]:
			dfs(ele)
	
def bfs(s): 
	que = deque([s]) # deque 선언과 동시에 start 를 []안에 저장시킨다.
	visited[s] = True 
	while que: 
		x = que.popleft() 
		print(x, end= ' ') 
		for ele in graph[x]: 
			if not visited[ele]: 
				que.append(ele) 
				visited[ele] = True
				
visited=[False]*(n+10)
dfs(s)
print()
visited=[False]*(n+10)
bfs(s)
		