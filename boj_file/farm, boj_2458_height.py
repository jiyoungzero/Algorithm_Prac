import sys
sys.setrecursionlimit(300000)
n, m = map(int, sys.stdin.readline().split())
height_t = [[] for _ in range(n + 1)]
height_s = [[] for _ in range(n + 1)]
cnt = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    height_t[a].append(b)
    height_s[b].append(a)
	
def dfs_t(x):
    visited[x] = 1
    global tall

    for i in height_t[x]:
        if not visited[i]:
            tall += 1
            dfs_t(i)
    return tall


def dfs_s(x):
    visited[x] = 1
    global short

    for i in height_s[x]:
        if not visited[i]:
            short += 1
            dfs_s(i)
    return short

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    tall = short = 0
    temp1 = dfs_t(i)

    visited = [0] * (n + 1)
    temp2 = dfs_s(i)
    if temp1 + temp2 == n - 1:
        cnt += 1

print(cnt)









		
	