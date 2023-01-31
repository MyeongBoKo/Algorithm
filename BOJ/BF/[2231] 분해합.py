n = int(input())
for i in range(1, n+1):
    x = i
    a = i
    while x:
        a += x%10
        x//= 10
    if a == n:
        break
else:
    print(0)
    exit(0)
print(i)
