n = int(input())
row = [0]*n
ans = 0
ver = [False]*(n+1)
diag1 = [False]*(2*n+1)
diag2 = [False]*(2*n+1)

def n_queen(x):
    global ans
    if x == (n+1):
        ans += 1
        return ans
    else:
        for i in range(1,n+1):
            if ver[i] or diag1[x+i] or diag2[x -i+n]:continue
            ver[i] = diag1[x+i] = diag2[x-i+n] = True
            n_queen(x+1)
            ver[i] = diag1[x+i] = diag2[x-i+n]=False #백트래킹

n_queen(1)
print(ans)
