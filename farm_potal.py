#  윌리는 좌표 X에서 좌표 Y까지 포탈을 이용하여 이동하려고 한다.
#  포탈을 이용하면 좌표 A에서 좌표 A+1, A-1, 2*A 중 한 좌표로 이동할 수 있다. 
#  X와 Y를 입력받아 좌표 X에서 좌표 Y까지 이동하기위한 포탈의 최소 사용 횟수를 구해보자



# 입력
# 첫 줄에 X,Y가 공백을 사이에 두고 주어진다. 두 값 모두 0 이상 10만 이하이다.


from collections import deque 
x, y = tuple(map(int, input().split()))
que = deque()
visited = [0]*200030 # x,y의 범위가 20만이므로 둘 다 합치고 여유분 30
visited[x] = 1 # 일단 x에서 시작한다고 보고 이때 방문처리로 해줌
que.append(x) # 큐에 처음 위치 넣고 while문으로 돌려서 bfs시작!
	
while que:
	k = que.popleft() # 시작위치 꺼내주고 세가지 경우의 수로 돌리기, 두번째부터는 visited[nx] == 0가 성립하는지도 확인
	if k+1<=200000 and visited[k+1] == 0:
		visited[k+1] = visited[k]+1
		que.append(k+1)
	if k-1>=0 and visited[k-1] == 0:
		visited[k-1] = visited[k]+1
		que.append(k-1)
	if k*2<=200000 and visited[k*2] == 0:
		visited[k*2] = visited[k]+1
		que.append(k*2)
print(visited[y]-1)