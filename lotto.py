import random

ext = set()

lists = []
list_count = 0

while True:
    lo_list = []
    while True:
        ran = random.randint(1, 45)
        if ran in ext:
            continue
        lo_list.append(ran)
        ext.add(ran)
        if len(lo_list) == 6:
            lists.append(lo_list.copy())
            list_count += 1
            break
    if list_count == 5:
        break

for i in lists:
    i.sort()
    print(i)