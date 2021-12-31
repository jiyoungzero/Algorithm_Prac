row, col = tuple(map(int, input().split()))
max_area = 0
dxs = [0, 0, 1, -1]
dys = [-1, 1,0, 0]
maze = [list(map(int, input().split())) for _ in range(row)]
cnt = 0

def wall(w_cnt):
    if w_cnt == 3:
        dfs()
    else:
        w_cnt+=1
        wall(w_cnt)
        dfs()
        
def in_range(x, y): 
    return 0 <= x and x < col and 0 <= y and y < row

def dfs():
    for x in range(row):
        for y in range(col):
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and maze[x][y] == 0 and maze[nx][ny] == 2:
                    maze[x][y] == 2