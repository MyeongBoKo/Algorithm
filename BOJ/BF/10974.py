n = int(input())
nums = [i for i in range(1, n+1)]
ans = []

def dfs():
    if len(ans) == n:
        print(*ans)
        return
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()

dfs()
