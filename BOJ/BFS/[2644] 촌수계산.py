from collections import deque

def bfs(s):
    queue=deque([s])
    visited[s]=True

    while queue:
        v=queue.popleft()
          for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                res[i]=res[v]+1
                visited[i]=True

n=int(input())
a,b=map(int,input().split())
m=int(input())

graph=[[] for _ in range(n+1)]
visited = [False] * (n + 1)
res=[0]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)
if res[b]>0:
    print(res[b])
else:
    print(-1)
