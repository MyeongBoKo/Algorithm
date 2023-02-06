import sys

input = sys.stdin.readline

def dfs(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4

    else:
        return dfs(num-1) + dfs(num-2) + dfs(num-3)
    

T = int(input())
for _ in range(T):
    num = int(input())
    print(dfs(num)) 
