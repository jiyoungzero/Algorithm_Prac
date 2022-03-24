n, k = map(int, input().split())
arr = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v) # i-1 과 같은 것이 있어서 왠만하면 arr를 1부터 시작하도록 [0,0]처음에 추가하기

print(d[n][k])