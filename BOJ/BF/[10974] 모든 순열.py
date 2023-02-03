def dfs():
    if len(ans)==n:
        print(*ans)
        return

    for i in range(1,n+1):
        if not visited[i]:
            ans.append(i)
            visited[i] = True
            dfs()
            visited[i] = False
            ans.pop()
            

n = int(input())
result = [i for i in range(1, n+1)]
visited  = [False]*(n+1)
ans = []
dfs()
    

