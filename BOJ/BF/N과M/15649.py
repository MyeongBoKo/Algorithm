n,m=map(int,input().split())
visited = [False]*(n+1)
ans = []

def dfs(cnt):
    if cnt == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            dfs(cnt+1)
            visited[i] = False
            ans.pop()

dfs(0)
