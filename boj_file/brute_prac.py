
row, col = tuple(map(int, input().split()))

lst = [ list(input()) for _ in range(row)]
re_lst =[]

for i in range(row - 7):
    for j in range(col - 7):
        f_B = 0
        f_W = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) %2 == 0:    
                    if lst[a][b] != "W":
                        f_W += 1
                    if lst[a][b] != "B":
                        f_B += 1
                else:
                    if lst[a][b] != "B":
                        f_W += 1
                    if lst[a][b] != "W":
                        f_B += 1    
        re_lst.append(f_W)
        re_lst.append(f_B)                    

print(min(re_lst))