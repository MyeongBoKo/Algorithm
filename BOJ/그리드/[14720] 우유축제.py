import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    if arr[i] == ans % 3:
        ans += 1

print(ans)
