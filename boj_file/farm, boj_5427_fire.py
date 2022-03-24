from collections import deque

n = int(input())
case = [0]*n
que_p = deque([])
que_f = deque([])
dxs, dys = [-1,1,0,0],[0,0,1,-1]
ans = 0

for i in range(n):
	w, h = tuple(map(int, input().split()))
	case[i] = [input().split() for _ in range(h)]
	matrix_f = [ [0]*w for _ in range(h)]
	matrix_p = [ [0]*w for _ in range(h)]
	for j in range(h):
		for k in range(w):
			if case[i] == '*':que_f.append([j,k])
	for j in range(h):
		for k in range(w):
			if case[i] == '@':que_p.append([j,k])

	def bfs_f():
		global que_f, dxs, dys
		while que_f:
			x, y = que_f.popleft()
			for i in range(4):
				nx, ny = dxs[i]+x, dys[i]+y
				if 0<= nx<n and 0<=ny < n and matrix_f[nx][ny] == 0:
					matrix_f[nx][ny] = matrix_f[x][y] + 1
					que_f.append([nx,ny])
	def bfs_p():
		global que_f, dxs, dys
		while que_p:
			x, y = que_p.popleft()
			for i in range(4):
				nx, ny = dxs[i]+x, dys[i]+y
				if 0<= nx,ny < n and matrix_p[nx][ny] == 0:
					matrix_p[nx][ny] = matrix_p[x][y] + 1
					que_p.append([nx,ny])	
	bfs_f()
	bfs_p()
	
	for ele_f in matrix_f: