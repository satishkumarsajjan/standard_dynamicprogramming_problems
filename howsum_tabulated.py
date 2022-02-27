def howsum_tabulated(targetsum,arr):
    new_arr=[None for i in range(targetsum+1)]
    new_arr[0]=[]
    for i in range(targetsum+1):
        if new_arr[i]!=None:
            for j in arr:
                if i+j<=targetsum:
                    temp=new_arr[i].copy()
                    temp.append(j)
                    new_arr[i+j]=temp
    return new_arr[-1]

print(howsum_tabulated(8,[1,2,3]))
