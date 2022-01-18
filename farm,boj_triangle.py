n = int(input())
cnt = 0
long = 0
for i in range(1, n):
	for j in range(i, n):
		k = n-(i+j)
		long = max(i, j, k)
		if long < n-long and j<=k:
			cnt+=1
		else:
			continue
print(cnt)