n = int(input())
arr = list(map(int, input().split()))
m = int(input())
s =0 
cnt = 0
stop = 0
for a in range(n):
	s= 0
	while(s <= m):
		for b in range(a,n):
			s+=arr[b]
			stop = b
	cnt += n-stop+1
print(cnt)