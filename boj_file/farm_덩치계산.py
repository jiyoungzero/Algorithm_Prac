# 완전탐색 
n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
ans = [n for _ in range(n)]

for i in range(n):
	for j in range(i, n):
		if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
			ans[i] -= 1
		elif (lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]) or (lst[i][0] < lst[j][0] and lst[i][1] > lst[j][1]):
			ans[i] -= 1 
			ans[j] -= 1
		elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
			ans[j] -= 1

print(ans)
