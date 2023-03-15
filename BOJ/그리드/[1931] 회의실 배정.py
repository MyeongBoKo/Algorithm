import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr = sorted(arr, key = lambda a:a[0]) 
arr = sorted(arr, key = lambda a:a[1]) 

cnt = 1
end = arr[0][1]
for i in range(1,n):
    if arr[i][0] >= end:
        cnt += 1
        end = arr[i][1]

print(cnt)
