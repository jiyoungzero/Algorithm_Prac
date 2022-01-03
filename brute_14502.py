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
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]
max_result = 0
def bfs():
    global max_result
    copy = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = s[i][j]
    result = 0
    arr = []
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                arr.append([i, j])
    while arr:
        a, b = arr[0][0], arr[0][1]
        del arr[0]
        for i in range(4):
            ax = a + dxs[i]
            ay = b + dys[i]
            if 0 <= ax and 0 <= ay and ax < n and ay < m:
                if copy[ax][ay] == 0:
                    copy[ax][ay] = 2
                    arr.append([ax, ay])
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if s[i][j] == 0:
                s[i][j] = 1
                wall(cnt + 1)
                s[i][j] = 0
n, m = map(int, input().split())
for i in range(n):
    s.append(list(map(int, input().split())))
wall(0)
print(max_result)