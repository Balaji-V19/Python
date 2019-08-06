if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    """maxs=0
    sec_max=0
    for i in range(n):
        if arr[i] > maxs:
            maxs = arr[i]
        else:
            continue
    for j in range(n):
        if arr[j] > sec_max and arr[j] < maxs:
            sec_max = arr[j]  
        else:
            continue              
    print(sec_max)   """
    z=max(arr)
    while max(arr)==z:
        arr.remove(z)
    print(max(arr))              

             

