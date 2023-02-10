N = int(input())
V = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
count = 0

for _ in range(V):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global count
    visited[start] = True
    count += 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count-1)
