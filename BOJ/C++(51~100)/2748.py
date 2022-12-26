def fibo2(n):
    global memo
    if len(memo)>n:
        return memo[n]
    else:
        memo.append(fibo2(n-1) + fibo2(n-2))
        return memo[n]

memo = [0,1]
print(fibo2(int(input())))
