import sys

INT_MAX = sys.maxsize

row, col = tuple(map(int, input().split()))
cnt = 0
min_num = INT_MAX

lst = [list(input().split()) for _ in range(row)]

def in_range(x, y):
    return (x+7) < row and (y+7)< col

for x in range(row):
    for y in range(col):
        if in_range(x,y):
            if not (lst[x][y] == "B" and lst[x][y+1] == "W" and lst[x+1][y] == "W"):
                cnt += 1
            elif not (lst[x][y] == "W" and lst[x][y+1] == "B" and lst[x+1][y] == "B"):
                cnt += 1
        if not in_range(x, y):
            break
    ans = min(min_num, cnt)    

print(ans)