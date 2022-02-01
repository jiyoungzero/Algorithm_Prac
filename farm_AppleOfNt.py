N,M = tuple(map(int, input().split()))
arr = [ list(input()) for _ in range(N) ] # 리스트로 바꿔서 입력받으면 str assignment error 해결 가능 !!!
stop = 0
for n in range(N-1,-1,-1): # 행의 마지막부터
	for m in range(M): # 열은 순서대로
		if arr[n][m] == '.':
			for i in range(n-1,-1,-1): # arr[n][m] 위에 검사
				if arr[i][m] == 'o':
					arr[i][m] = '.'
					arr[n][m] = 'o'
					break
				elif arr[i][m] == '#':break
				

for i in range(N):
	for j in range(M):
		print(arr[i][j],end='')
	print()