from collections import Counter

word = list(input().upper())
val = Counter(word).most_common()

for i in val:
    if val.count(val[i][1]) >= 2:
        print("?")
    else:
        print(val[0][0])

