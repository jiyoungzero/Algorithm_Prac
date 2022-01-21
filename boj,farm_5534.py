N = int(input())
board = input()
arr =[input() for _ in range(N)]
ans = 0
flag = False

for i in range(N): # 기존표지 수만큼
	flag = False
	for j in range(len(arr[i])): # 표지 하나당 검사할 수
		for d in range(1,len(arr[i])): # 간격
			if len(arr[i]) <= j+d*(len(board)-1): # 마지막 글자까지 표지인덱스에 들어가는지
				continue
			allsame = 0
			for k in range(len(board)):
				if board[k] == arr[i][j+k*d]:
					allsame+=1 # 일치하면 ++
			if allsame == len(board):
				flag = True
	if flag == True:
		ans += 1			

print(ans)
				