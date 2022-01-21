n = int(input())
graph = []
value = []

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
cnt = 0
result = 0

for i in range(n):
	graph.append(list(map(int, input())))
	
def dfs(x, y):
	#범위 내에 있는가
	if x < 0 or x >= n or y < 0 or y >= n:	
		return False
	# x, y가 집이 있다면
	if graph[x][y] == 1:
		global cnt
		cnt += 1
		# 방문했으니까 빈곳으로 만들고 방향 검사
		graph[x][y] = 0
		for i in range(4):
			nx = x + dxs[i]
			ny = y + dys[i]
			# 여기서 dfs
			dfs(nx, ny)
		return True
	return False

for i in range(n):
	for j in range(n):
		if dfs(i,j) == True:
			value.append(cnt)
			result += 1
			cnt = 0
			
print(result)			
value.sort()
for i in range(len(value)):
	print(value[i])