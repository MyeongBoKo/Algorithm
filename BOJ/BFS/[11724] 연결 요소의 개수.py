from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    
    q = deque([start])
    visited[start] = True
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    
    

N, M = map(int, input().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
cnt = 0

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)
