ans = 0
arr = []
for _ in range(10):
    arr.append(int(input()))

for i in arr:
    ans += i
    if ans >= 100:
        if ans-100 > 100-(ans-i):
            ans -= i
        break
print(ans)
