result = []
ans = [i for i in range(1,10000)]
for i in range(1, 10000):
    x = i
    r = i
    while x:
        r += x%10
        x //= 10
    if r <= 10000:
        result.append(r)

result.sort()
set(result)

for i in ans:
    if i not in result:
        print(i)
