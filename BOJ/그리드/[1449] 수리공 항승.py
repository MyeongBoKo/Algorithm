n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

start = arr[0]
cnt = 1

for location in arr:
    if location not in range(start, start+l):
        start = location
        cnt += 1

print(cnt)
