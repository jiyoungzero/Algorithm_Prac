from collections import deque

n, m = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
c = 0
dxs = [0,0,1,-1]
dys = [1,-1,0,0]

def bfs():
    de = deque()
    de.append([0,0])
    ch = [[-1]*m for _ in range(n)]
    ch[0][0] = 0
    