import sys
input = sys.stdin.readline

n = int(input())

count = 1
stack = []
ans = []
temp = True

for _ in range(n):
    data = int(input())

    while count <= data:
        stack.append(count)
        ans.append('+')
        count += 1

    if stack[-1] == data:
        stack.pop()
        ans.append('-')
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in ans:
        print(i)
