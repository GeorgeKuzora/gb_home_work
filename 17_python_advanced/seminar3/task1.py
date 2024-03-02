from collections import Counter

lst = [
    1,
    2,
    3,
]
c = Counter(lst)
res = [x for x in c if c[x] > 1]
print(res)
