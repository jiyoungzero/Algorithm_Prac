# 완전탐색 
n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
ans = [n for _ in range(n)]
n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
ans = []
bigger = 0

for i in range(n):
	for j in range(n):
		if i != j and lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
			bigger += 1 
	ans.append(bigger+1)
	bigger = 0

for ele in ans:
	print(ele, end=' ')
