row, col = tuple(map(int, input().split()))
max_area = 0

maze = [list(map(int, input().split())) for _ in range(row)]

for i in range(row):
    for j in range(col):
        if maze[i][j] == '0' and maze[i+1][j] == '2':
            