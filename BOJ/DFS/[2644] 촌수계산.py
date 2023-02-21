def dfs(A):
    visited[A] = True
    for i in graph[A]:
        if not visited[i]:
            res[i] = res[A]+1
            dfs(i)


N = int(input())
a, b = map(int, input().split())
T = int(input())

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
res = [0]*(N+1)

for _ in range(T):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a)

if res[b]!=0:
    print(res[b])
else:
    print(-1)
