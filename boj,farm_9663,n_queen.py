n = int(input())
row = [0]*n
ans = 0
ver = [False]*(n) # 열 배열 ver[x] = True 이면 
diag1 = [False]*(2*n) # / 중 겹치는 게 있는지 
diag2 = [False]*(2*n) # \ 중 겹치는 게 있는지

def n_queen(x):
    global ans
    if x == (n):
        ans += 1
        return ans
    else:
        for i in range(0,n): # (x, i)
            if ver[i] or diag1[x+i] or diag2[x -i+n]:continue
            ver[i] = diag1[x+i] = diag2[x-i+n] = True
            n_queen(x+1)
            ver[i] = diag1[x+i] = diag2[x-i+n]=False #백트래킹

n_queen(0)
print(ans)
