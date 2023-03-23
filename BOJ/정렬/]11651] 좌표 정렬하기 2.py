import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])

arr = sorted(arr, key = lambda a:(a[1], a[0]))

for i in arr:
    print(i[0], i[1])
