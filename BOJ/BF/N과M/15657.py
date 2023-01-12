n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []

def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, n):
        ans.append(num[i])
        dfs(i)
        ans.pop()

dfs(0)
