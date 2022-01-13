# node, branch, first node
n, m, v = tuple(map(int, input().split()))

# depth first search
def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i) # 깊이탐색은 재귀로 해결

# breadth first search
def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visitied[i] = True #너비탐색은 큐에 저장 후 반복하며 탐색

