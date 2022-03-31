# bfs
from collections import deque
import sys

n = int(input())
w, h, k = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

print(graph)
