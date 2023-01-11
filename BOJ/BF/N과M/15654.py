n, m = map(int, input().split())
num = list(map(int, input().split()))

ans = []
num.sort()
def dfs():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in num:
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()

dfs()
        
