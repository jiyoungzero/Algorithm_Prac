import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = []
ans = 0
for i in range(len(arr)):
	for j in range(i, len(arr)+1):
		sum_arr.append(sum(arr[i:j]))

for ele in sum_arr:
	if ele == m:
		ans+=1
print(ans)