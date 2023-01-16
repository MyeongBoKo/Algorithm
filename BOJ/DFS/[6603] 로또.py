def dfs(depth, start):
    if depth == 6:
        print(*ans)
        return

    for i in range(start, arr[0]):
        ans.append(arr[i+1])
        dfs(depth+1, i+1)
        ans.pop()

while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    ans=[]
    dfs(0,0)
    print()
    
        
