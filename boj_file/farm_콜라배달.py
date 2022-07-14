# 완전탐색

n = int(input())
ans = []
three = n // 3
five = n//5
min_ans = 0
for i in range(three+1):
	for j in range(five+1):
		if (i*3 + j*5) == n:
			ans.append(i+j)
		else:
			continue
if len(ans) > 0:
	print(min(ans))
else:
	print(-1)