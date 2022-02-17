arr = [int(input()) for i in range(9)]

for i in range(9):
    if len(arr) <= 9:
        break

    for j in range(i+1,9):
        if 100 == sum(arr) - (arr[i] + arr[j]): 
            temp1,temp2=arr[i],arr[j]
            arr.remove(temp1)
            arr.remove(temp2)
			
            arr.sort() 
            for ele in arr:
               print(ele)
            break