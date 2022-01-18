n = int(input())
arr = [input() for _ in range(n)]
h=[]
p=[]
s=[]# 가위, 바위, 보
h_cnt, p_cnt, s_cnt = 0,0,0
ans = 0
#prefix 
for i in range(n):
	if arr[i] == 'P':
		p_cnt+=1
		p.append(p_cnt)
		h.append(h_cnt)
		s.append(s_cnt)
	elif arr[i] == 'H':
		h_cnt += 1
		h.append(h_cnt)
		s.append(s_cnt)
		p.append(p_cnt)
	else:
		s_cnt += 1
		s.append(s_cnt)
		p.append(p_cnt)
		h.append(h_cnt)

# i 번째까지의 가위바위보 중 최대값, 그 이후의 가위바위보 중 최대값을 더한 값이 최대가 되는 경우
for i in range(n):
	for j in range(i, n):
		l=max(p[i],h[i],s[i])
		r=max(p[n-1]-p[j],h[n-1]-h[j],s[n-1]-s[j])
		ans = max(ans, l+r)
		
print(ans)	