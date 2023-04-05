import sys
input = sys.stdin.readline

arr = [25, 10, 5, 1]
t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    for i in arr:
        ans.append(n//i)
        n %= i
    print(*ans)
