n = int(input())
row = [0]*n
ans = 0

def n_queen(x):
	global ans
	if x == n:
		ans += 1
		return ans
	else:
		for i in range(n):
			# (x,i) / (j, row[j])
			row[x] = i
			for j in range(x):
				if i != row[j] and (x-i) != (j-row[j]) and (x+i) != (j+row[j]):
					n_queen(x+1)
n_queen(0)
print(ans)
