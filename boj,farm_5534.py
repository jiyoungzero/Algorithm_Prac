n = int(input())
string = input()
arr =[input() for _ in range(n)]
cnt, ans, dist = 0,0,0
flag = False

for ele in arr:
	m_dist = len(ele)//len(string)
	for i in range(len(ele)-len(string)+1):# 시작지점 범위
		if flag==True:break
		for j in range(1,m_dist+1):
			if flag==True:
				cnt = 0
				break
			for k in range(len(string)): # 표지글자 비교
				if string[k] == arr[i+j*k]:
					cnt+=1
			if cnt == len(string):
				flag = True
	if flag == True:
		ans+=1
				
print(ans)