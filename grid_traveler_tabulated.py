def grid_traveler(x,y):
    arr=[[0 for i in range(y)] for j in range(x)]
    for i in range(y):
        arr[0][i]=1
    for i in range(x):
        arr[i][0]=1
    for i in range(1,x):
        for j in range(1,y):
            arr[i][j]=arr[i-1][j]+arr[i][j-1]
    return arr

for row in grid_traveler(2,3):
    print(*row, sep="\t")