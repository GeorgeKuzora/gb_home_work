from itertools import combinations

both = list1 + list2
com = combinations(both, 2)
count = 0
for l1, l2 in com:
    if l1 == l2:
        count += 1
print(f"Количество совпадающих чисел: {count}")
