from sys import stdin, stdout

input = stdin.readline
print = stdout.write

result = []
for _ in range(int(input())):
    result.append(list(input().split()))

result.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in result:
    print(i[0]+'\n')
