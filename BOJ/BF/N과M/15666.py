N, M = map(int, input().split())
num = sorted(list(set(map(int, input().split()))))
ans = []

def dfs(start):
    if start == M:
        print(*ans)
        return

    for i in range(len(num)):
        if start == 0 or ans[-1]<=num[i]:
            ans.append(num[i])
            dfs(start+1)
            ans.pop()

dfs(0)
