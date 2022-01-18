n = int(input())
cnt = 0

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            if i<=j and j<=k and k<i+j and (i+j+k) == n:
                cnt+=1
            else:
                continue
print(cnt)