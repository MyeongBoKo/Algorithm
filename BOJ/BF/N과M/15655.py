n,m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

ans = []

def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(start, n):
        if num[i] not in ans:
            ans.append(num[i])
            dfs(i+1)
            ans.pop()

dfs(0)
