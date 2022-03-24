a, b, c, n = map(int, input().split())
m_value = int(n / min(a, b, c))
ans = 0

# 삼중 for문 이용
for i in range(n//a+1):
	for j in range(n//b+1):
		for k in range(n//c+1):
			if (i*a)+(b*j)+(k*c) == n:
				ans += 1
if ans > 0:
	print(1)
else:
	print(0)