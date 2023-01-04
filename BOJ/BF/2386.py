while True:
    answer = input()
    if answer == '#':
        break

    a, b =answer[0], answer[1:].lower()
    cnt = b.count(a)
    print(a,cnt,end= ' ')
    print()
