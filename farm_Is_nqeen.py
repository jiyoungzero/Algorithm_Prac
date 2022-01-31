n = int(input())
arr = [input() for _ in range(n)]
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
			if arr[x][i] == 'Q':
				ver[i] = diag1[x+i] = diag2[x-i+n] = True
			if ver[i] or diag1[x+i] or diag2[x-i+n]:continue
			else: is_nqueen(x+1)
				
is_nqueen(0)
if flag:print("YES")
else: print("NO")