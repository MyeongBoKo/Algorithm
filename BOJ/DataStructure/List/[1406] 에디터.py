import sys

stack_first = list(input())
stack_last = []

for i in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == 'L' and stack_first:
        stack_last.append(stack_first.pop())
    elif command[0] == 'D' and stack_last:
        stack_first.append(stack_last.pop())
    elif command[0] == 'B' and stack_first:
        stack_first.pop()
    elif command[0] == 'P':
        stack_first.append(command[1])

print(''.join(stack_first + list(reversed(stack_last))))
