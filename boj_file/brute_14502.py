# import copy

# row, col = tuple(map(int, input().split()))
# max_area = 0
# dxs = [0, 0, 1, -1]
# dys = [-1, 1,0, 0]
# maze = [list(map(int, input().split())) for _ in range(row)]
# cnt = 0

# def wall(w_cnt):
#     if w_cnt == 3:
#         dfs()
#         return
#     else:
#         for i in range(row):
#             for j in range(col):
#                 if maze[i][j] == 0:
#                     maze[i][j] = 1
#                     w_cnt+=1
#                     wall(w_cnt)
#                 # 왜 maze[i][j] = 0로 하지

        
# def in_range(x, y): 
#     return 0 <= x and x < col and 0 <= y and y < row

# def dfs():
#     for x in range(row):
#         for y in range(col):
#             for dx, dy in zip(dxs, dys):
#                 nx, ny = x + dx, y + dy
#                 if in_range(nx, ny) and maze[x][y] == 0 and maze[nx][ny] == 2:
#                     maze[x][y] == 2

s = []
dxs = [0, 0, -1, 1] # x축은 행
dys = [-1, 1, 0, 0] # y축은 열
max_result = 0
def bfs():
    global max_result
    copy = [[0] * m for i in range(n)] # 맵 복사본
    for i in range(n):
        for j in range(m):
            copy[i][j] = s[i][j] # 맵 복사
    result = 0
    arr = [] # 바이러스 개수 배열
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                arr.append([i, j]) # 만약 맵 복사본에서 바이러스가 나오면 그 위치[i,j] arr에 저장
    while arr: # 바이러스 개수를 담은 배열의 수만큼 돌리나?????????
        a, b = arr[0][0], arr[0][1] # a는 바이러스 x축, b는 y축
        del arr[0] # 하나 검사 마쳤으니까 del 
        for i in range(4):
            nx = a + dxs[i]
            ny = b + dys[i]
            if 0 <= nx and 0 <= ny and nx < n and ny < m:
                if copy[nx][ny] == 0:
                    copy[nx][ny] = 2 # 벽이 빈 공간이면 바이러스 2로 만들고 배열에 추가
                    arr.append([nx, ny]) # 바이러스 위치는 arr에 추가
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)

def wall(cnt):
    if cnt == 3: # 벽을 3개 이미 세웠다면 dfs 함수로 넘어가고
        bfs()
        return
    for i in range(n):
        for j in range(m): # 모든 칸을 돌면서 벽을 설치해 본다.
            if s[i][j] == 0:
                s[i][j] = 1
                wall(cnt + 1)
                s[i][j] = 0 # 하나의 케이스가 끝이 나면 다시 빈공간으로 돌려놓기
n, m = map(int, input().split())
for i in range(n):
    s.append(list(map(int, input().split()))) 
wall(0)
print(max_result)