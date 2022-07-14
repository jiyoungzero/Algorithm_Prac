# 완전탐색

n = int(input())
ans = 0
max_num = n // 2

if n % 5 == 0:
	ans = n//5
	print(ans)
elif n % 5 != 0 and n % 3 == 0:
	if n // 5 >= 3:
		ans = n//5  + (n % 5)//3
		print(ans)
	else:
		ans = n//3
		print(ans)

else:
	print(-1)