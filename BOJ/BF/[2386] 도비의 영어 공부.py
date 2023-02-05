while True:
    result = input().lower()
    if result == '#':
        break

    count = 0
    for i in result[1:]:
        if i == result[0]:
            count += 1

    print(result[0], count)
    

