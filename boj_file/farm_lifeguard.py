# 안전한 시간이(한 명의 라이프가드라도 있는 시간) 가장 길도록 라이프가드를 해고할 예정

import copy
n = int(input())
m_time = 0
cnt = 0
arr = [False]*1001
ans = []
t = []
for _ in range(n):
	s, f = map(int, input().split())
	t.append([s,f])

# 총시간
for i in range(n):
	for j in range(t[i][0], t[i][1]):
		arr[j] += 1

c_arr = copy.copy(arr)

# 한명씩 해고했을 때 
for i in range(n):
	cnt = 0
	for j in range(t[i][0], t[i][1]):
		c_arr[j] -= 1
	for ele in c_arr:
		if ele >= 1:
			cnt += 1
	ans.append(max(m_time, cnt))
	for j in range(t[i][0], t[i][1]):
		c_arr[j] +=1 	
	
print(max(ans))
	