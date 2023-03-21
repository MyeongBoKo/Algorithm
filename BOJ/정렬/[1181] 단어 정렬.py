import sys
input = sys.stdin.readline

n = int(input())
arr = [str(input().strip()) for _ in range(n)]

arr = list(set(arr))
arr.sort()
arr = sorted(arr, key = lambda a:len(a))

for i in arr:
    print(i)
