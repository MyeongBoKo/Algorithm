while True:
    arr = list(map(int, input().split()))
    if arr[0] == -1:
        break

    count = 0

    for i in arr:
        if i == 0:
            pass
        elif i*2 in arr:
            count += 1

    print(count)
