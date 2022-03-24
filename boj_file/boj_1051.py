import sys

n, m = tuple(map(int, input().split()))
arr = [list(map(int, input())) for _ in range(n)]
ans = -sys.maxsize
def in_range(x,y):
	return x>=0 and x<n and y>=0 and y<m # x,y >= 0 이여야 넓이가 1 인 것도 포함

# 모든 좌표를 돌면서 그 숫자가 왼쪽위의 꼭짓점을 가지는 사각형 중 가장 큰 값을 저장
for i in range(n):
	for j in range(m):
		for k in range(min(n,m)): # 둘 중 작은 값
			if in_range(i+k, j+k) and arr[i][j] == arr[i+k][j+k] ==arr[i][j+k]==arr[i+k][j] :
				ans = max(ans, (k+1)**2)
				
print(ans)		