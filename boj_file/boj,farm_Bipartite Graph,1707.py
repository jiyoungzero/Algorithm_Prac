import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = tuple(map(int, input().split()))
graph = [[]*v for _ in range(v+1)]
visited = [False]*(v+1)
flag = False

for _ in range(e):
	a, b = tuple(map(int, input().split()))
	graph[a].append(b)
	graph[b].append(a)
	
# 인접한 정점끼리 두가지 색으로 칠하는 dfs함수
def dfs(x, c):
	global visited
	visited[x] = c # 색 배정
	for i in graph[x]:
		if not visited[i] :
			dfs(i, c*(-1)) # 다른 색으로 방문
		elif visited[i] == visited[x]:
			return False
	return True

for i in range(1, v+1):
	if not visited[i]:
		flag=dfs(i, 1)
		if not flag:break
print("YES" if flag else "NO")