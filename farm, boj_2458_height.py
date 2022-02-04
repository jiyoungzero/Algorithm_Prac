n, m = tuple(map(int, input().split()))
arr = []
f_arr = []
b_arr = []
visited = [False]*(n+1)
t_cnt, s_cnt = 0,0

for _ in range(m):
	a, b = tuple(map(int, input().split()))
	f_arr[a].append(b)
	b_arr[b].append(a)
	
def taller_dfs(x):
	global t_cnt
	if visited[x] == False:
		visited[x] = True
	for i in range(len(f_arr)):
		if visited[i] == False:
			t_cnt += 1
			taller_dfs(i)
	return t_cnt

def shorter_dfs(x):
	global s_cnt
	if visited[x] == False:
		visited[x] = True
	for i in range(len(b_arr)):
		if visited[i] == False:
			s_cnt += 1
			shorter_dfs(i)
	return s_cnt