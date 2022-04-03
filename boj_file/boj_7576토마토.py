from collections import deque
import sys

m, n = int(input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*(m+1) for _ in range(n+1)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
