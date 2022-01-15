from collections import deque

# node, branch, first node
n, m, v = tuple(map(int, input().split()))

# depth first search
def dfs(n):
    #현재 노드를 방문 처리
    print(n, end=' ')
    visited[n] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[n]:
        if not visited[i]:
            dfs(i) 

# breadth first search
def bfs(n):
    #큐 구현을 이해 deque 라이브러리 이용
    queue = deque([n])
    visited[n] = True    

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end =' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visitied[i] = True 

graph = [[] * (n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    # 인접한 것 연결
    graph[a].append(b)
    graph[b].append(a)
# 인접한 것들을 sort
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)




