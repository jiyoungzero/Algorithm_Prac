
# 확대를 원하는 배율 x 가 주어질 때, 기존의 이미지를 x배 만큼 확대해 주는 프로그램을 작성

n, m = map(int, input().split())
img = [input() for _ in range(n)]
x = int(input())
ans = []
cnt = 0
for i in range(n):
	for k in range(x):
		for j in range(m):
			for k in range(x):
				ans.append(img[i][j])
				
for ele in ans:
	cnt+=1
	print(ele, end='')
	if cnt == m*x :
		print()
		cnt = 0