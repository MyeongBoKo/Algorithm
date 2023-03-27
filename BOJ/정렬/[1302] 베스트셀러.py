import sys
input = sys.stdin.readline

n = int(input())
arr = {}

for _ in range(n):
    name = input().rstrip()

    if name not in arr:
        arr[name] = 1
    else:
        arr[name] += 1

max_value = max(arr.values())

best_arr = []

for name, number in arr.items():
    if number == max_value:
        best_arr.append(name)


print(sorted(best_arr)[0])
