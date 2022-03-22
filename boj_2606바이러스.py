import sys
from collections import deque

n = int(input())
pair = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
