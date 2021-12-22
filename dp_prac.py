n = int(input())
t = []
p = []
dp = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)

for a in range(n):
    for b in range(a,n):
        if j+lst[j][0]-1 <= (n-1):
            value += lst[j][1]
            if lst[j][0] == 1:
                j += 1
            else:
                j += lst[j][0]-1 
        else:
            break
        m_lst.append(value)
    j =0
    value = 0
print(max(m_lst))

        