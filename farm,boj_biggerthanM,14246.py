n = int(input())
arr = list(map(int, input().split()))
m = int(input())
s,cnt, stop = 0,0,0

for a in range(n):
	s = 0
	for b in range(stop,n):
    	# a부터 stop까지 
		s = sum(arr[a:b+1])
		if s > m : # m을 초과하는 합이 발생하는 끝지점 stop
			stop = b
			break
	if s>m:
		cnt += n-stop # 나머지 원소가 있는 만큼 더하기
print(cnt)