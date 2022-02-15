m, n = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
k = 10**9+7

def dp(x):
	dt = [0]*6000000
	dt[0] = 1
	for i in range(1, n):
		for j in range(m):
			if (i-arr[j]) >= 0:
				dt[i] += dt[i-arr[j]]
				dt[i]%=k
	return dt[x]
print(dp(n))