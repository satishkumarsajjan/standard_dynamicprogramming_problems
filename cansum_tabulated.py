def cansum_tabulated(targetsum,arr):
    new_arr=[False for i in range(targetsum+1)]
    new_arr[0]=True
    for i in range(targetsum+1):
        if new_arr[i]==True:
            for j in arr:
                if i+j<=targetsum:
                    new_arr[i+j]=True
                
    return new_arr[-1]


print(cansum_tabulated(8,[5,6,7]))
