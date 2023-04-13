import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

ans = []
for i in range(N):
    ans.append(arr[i]*(i+1))

print(max(ans))
