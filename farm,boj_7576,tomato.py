from collections import deque

n,m = map(int, input().split()) # n은 세로, m은 가로
matrix = [list(map(int, input().split())) for _ in range(n)] # 토마토 상태 입력받은 배열
queue = deque([]) # 좌표자체를 요소로 받으니까 deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0

# 모든 matrix를 돌면서 토마토(1)가 나오면 그 좌표를 queue에 append
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j]) 

def bfs():
    while queue: # 큐에 들어있는 토마토(1) 수만큼 돌림
        x, y = queue.popleft() # popleft 한 좌표 [x,y]
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0: # 상하좌우를 돌면서 in_range의 여부, matrix가 빈칸인지 알아봄
                matrix[nx][ny] = matrix[x][y] + 1 # 빈칸이라면 +1해서 표시하고 nx, ny 좌표는 append
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j == 0: # 만약에 matrix의 성분이 빈칸이 나온다면(익지못하는 상황)
            print(-1)
            exit(0)
    ans = max(ans, i)
print(ans - 1)