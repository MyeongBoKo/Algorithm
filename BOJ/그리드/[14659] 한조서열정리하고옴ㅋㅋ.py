import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = []

for i in range(n-1):
    cnt = 0
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            cnt += 1
        else:
            break
    ans.append(cnt)

print(max(ans))
    
