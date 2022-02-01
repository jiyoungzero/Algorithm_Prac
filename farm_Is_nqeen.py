n = int(input())
arr = [input() for _ in range(n)] # 입력한 nqueen 배열
ver = [False]*n # 열
diag1 = [False]*2*n # /
diag2 = [False]*2*n # \
ans = 0
flag = False

def is_nqueen(x):
	global ans
	if x == n:
		flag = True
		return flag
	else:
		for i in range(n):
			# 입력한 nqueen 배정을 보고 열, 대각선 검사
			if arr[x][i] == 'Q':
				ver[i] = diag1[x+i] = diag2[x-i+n] = True
			# 열, 대각선에 어떤 것도 위치하지 않았을 때, 
			if (not ver[i]) and (not diag1[x+i]) and (not diag2[x-i+n]): is_nqueen(x+1)
				
is_nqueen(0)
if flag:print("YES")
else: print("NO")
				

