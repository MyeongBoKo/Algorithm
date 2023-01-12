N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
visited = [False]*N
ans = []

def recursion():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    remember_num = 0
    
    for i in range(N):
        if not visited[i] and remember_num != num_list[i]:
            visited[i] = True
            ans.append(num_list[i])
            remember_num = num_list[i]
            recursion()
            visited[i] = False
            ans.pop()

recursion()
