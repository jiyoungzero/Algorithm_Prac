n = int(input())
arr = [input() for _ in range(n)]
ver = [False]*n # 열
hor = [False]*n # 행 
diag1 = [False]*2*n # /
diag2 = [False]*2*n # \
flag = True

def is_nqueen(x):
	global flag,ver, hor, diag1, diag2
	for i in range(n):
		if not flag:break
		for j in range(n):
			if arr[i][j] == 'Q':
				if ver[j] or hor[i] or diag1[i+j] or diag2[i-j+n] :
					flag = False
					break
				ver[j] = hor[i] = diag1[i+j] = diag2[i-j+n] = True

is_nqueen(n)
if flag:print("YES")
else:print("NO")
				

