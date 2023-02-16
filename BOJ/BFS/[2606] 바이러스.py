from collections import deque

def bfs(start):
    global cnt
    q = deque([start])
    visited[start] = True
    while q:
        v=q.popleft()

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

N = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
cnt = 0

for _ in range(int(input())):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(1)
print(cnt)
    
