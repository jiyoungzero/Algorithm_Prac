n,m = tuple(map(int, input().split()))
arr = [list(map(str, input().split())) for _ in range(n)]
stop = 0

for r in range(n-1,-1,-1):
	for c in range(m):
		if arr[r][c] == '.':
			for i in range(r-1,-1,-1):
				if arr[i][c] == 'o':
					arr[i][c] = '.'
					arr[r][c] = 'o'
					stop = 1
				elif arr[i][c] == '#' or arr[i][c] == '.':
					stop = 0
					continue
			if stop == 1:
				continue
				
for i in range(n):
	for j in range(m):
		print(arr[i][j])
	print()