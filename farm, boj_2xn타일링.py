# 메모이제이션 (배열) 사용
n = int(input())

def dp(x):
	dt = [0]*600000
	dt[0] = 0
	dt[1] = 1
	dt[2] = 2
	for i in range(3, n+1):
		dt[i] = (dt[i-1]+dt[i-2])%10007
	return dt[n]

print(dp(n))