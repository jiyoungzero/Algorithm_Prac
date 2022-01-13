n, m, v = tuple(map(int, input().split()))

# depth first search
def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i) # 깊이탐색은 재귀로 해결

            