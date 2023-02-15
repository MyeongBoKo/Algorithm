import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    global count
    visited[start] = 1
    ans[start] = count
    graph[start].sort(reverse=True)

    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)

N, M, R = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
ans = [0]*(N+1)
count = 1


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


    
dfs(R)

for j in ans[1:]:
    print(j)
