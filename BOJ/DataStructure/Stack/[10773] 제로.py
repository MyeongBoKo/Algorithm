import sys
input = sys.stdin.readline

k = int(input())

stack_arr = []
for _ in range(k):
    num = int(input())

    if num != 0:
        stack_arr.append(num)
    else:
        stack_arr.pop()

print(sum(stack_arr))
