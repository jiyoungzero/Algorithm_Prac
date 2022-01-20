#  (7, 10)구간을 색칠하고 윌리가 (4, 8)구간을 색칠하였다면 총 색칠된 구간의 길이는 6

a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))
arr = [False]*101
cnt = 0
for i in range(a, b):
	arr[i] = True
for j in range(c, d):
	arr[j] = True
for ele in arr:
	if ele == True:
		cnt+=1
		
print(cnt)