import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = 1
s_dp = [0]
ans = 0
for i in range(1,n):
	for j in range(i):
		if arr[i] == arr[j]:dp[j] = dp[i]
		elif arr[i] < arr[j]:
			for k in range(j):
				if arr[j] < arr[k] :
					s_dp.append(dp[k])
			m_dp = max(s_dp)
			dp[j] = m_dp+1
			x = max(dp)
			ans = max(ans, x)
			s_dp = [0] # 초기화
		elif arr[i] > arr[j]:
			for k in range(j):
				if arr[j] > arr[k] :
					s_dp.append(dp[k])
			m_dp = max(s_dp)
			dp[j] = m_dp+1
			x = max(dp)
			ans = max(ans, x)
			s_dp = [0] # 초기화	

print(ans+1)