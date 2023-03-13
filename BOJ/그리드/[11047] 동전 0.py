n, k = map(int, input().split())
coin_types = []
for _ in range(n):
    coin_types.append(int(input()))
coin_types.sort(reverse=True)

answer = 0
for coin in coin_types:
    answer += k//coin
    k %= coin

print(answer)
