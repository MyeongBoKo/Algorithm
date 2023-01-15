N,S = map(int,input().split())
nums = list(map(int, input().split()))
ans = []
visited = [False]*(N+1)
count = 0



def dfs(start):
    global count
    if sum(ans) == S and len(ans)>0:
        count += 1
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            ans.append(nums[i])
            dfs(i+1)
            visited[i] = False
            ans.pop()

dfs(0)
print(count)
