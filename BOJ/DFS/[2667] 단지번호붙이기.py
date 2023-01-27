n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

ans = []
count = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    global count
     
    if 0<=x<n and 0<=y<n:
        if graph[x][y] == 1:
            count += 1
            graph[x][y] = 0
            for i in range(4):
                dfs(x+dx[i], y+dy[i])
            return True

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            ans.append(count)
            count = 0

print(len(ans))
#ans.sort
for i in sorted(ans):
    print(i)
            
