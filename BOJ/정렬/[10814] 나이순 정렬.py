import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a, b = list(input().split())
    arr.append([int(a), b])

arr = sorted(arr, key = lambda a:a[0])

for i in arr:
    print(i[0], i[1])

    
