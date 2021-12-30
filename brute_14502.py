row, col = tuple(map(int, input().split()))
max_area = 0
dxs = [0, 0, 1, -1]
dys = [-1, 1,0, 0]
maze = [list(map(int, input().split())) for _ in range(row)]

def in_range(x, y): 
    return 0 <= x and x < col and 0 <= y and y < row

for x in range(row):
    for y in range(col):
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1    
        if cnt >= 3: