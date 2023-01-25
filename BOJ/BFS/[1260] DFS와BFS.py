# 인접리스트
from collections import deque

def dfs(start):
    visited[start]=True
    print(start,end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] =True

N,M,V=map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
bfs(V)

# 인접행렬
from collections import deque

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited1 = [False]*(N+1)
visited2 = [False]*(N+2)

def dfs(V):
    visited1[V] = True
    print(V, end= ' ')
    for i in range(1,N+1):
        if not visited1[i] and graph[V][i] == 1:
            dfs(i)

def bfs(V):
    q = deque([V])
    visited2[V] = True
    while q:
        V = q.popleft()
        print(V, end = ' ')
        for i in range(1, N+1):
            if not visited2[i] and graph[V][i]==1:
                q.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)
