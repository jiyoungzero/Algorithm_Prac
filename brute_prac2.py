n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
m_lst = []
j = 0 
value = 0
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

        