n, m = tuple(map(int, input().split()))
arr = [list(input()) for _ in range(n)]
cnt = 0
flag = False
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
# 구현 방식 : R을 for문을 통해서 찾고 위, 아래, 왼쪽, 오른쪽으로
# 벽(#)을 만날 때까지 이동
# 이동 중에 O을 만나면 break.
# 이때 B가 O을 만나거나, 이동횟수(cnt)가 10이 넘어가면 -1출력


def in_range(x, y):
    return x >= 1 and y >= 1 and x < n-1 and y < m-1


def dfs():
    if cnt > 10:
        flag = False
        return flag
    for i in range(1, n-1):
        for j in range(1, m-1):
            if arr[i][j] == 'R':
                for k in range(4):
                    nx, ny = i+dxs[k], j+dys[k]
                    while arr[nx][ny] == '#':
                        if in_range(nx, ny):  # 벽을 만나기 전까지 쭉 이동하는 거 해결해야 함
