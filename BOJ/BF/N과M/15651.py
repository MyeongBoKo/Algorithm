n,m=map(int,input().split())
ans = []

def dfs(cnt):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(cnt+1, n+1):
            ans.append(i)
            dfs(cnt)
            ans.pop()
dfs(0)
