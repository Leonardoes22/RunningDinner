import itertools
import random

def random_product(*args, repeat=1):
    "Random selection from itertools.product(*args, **kwds)"
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(map(random.choice, pools))


appetizers = set(range(1,5))
main_dish = set(range(5,9))
dessert = set(range(9,13))

print(appetizers)
print(main_dish)
print(dessert)
print("\n\n\n")

#events = itertools.product(appetizers,main_dish,dessert)
used_groups = []

first_event = []

used_main = set()
used_dessert = set()

for pair in appetizers:
    group = random_product({pair},main_dish-used_main,dessert-used_dessert)
    first_event.append(group)
    used_groups.append(group)
    used_main.add(group[1])
    used_dessert.add(group[2])


second_event = []
used_appetizers = set()
used_dessert = set()
for pair in main_dish:
    done = False
    while not done:
        group = random_product(appetizers-used_appetizers,{pair},dessert-used_dessert)
        if group not in used_groups:
            done = True
    second_event.append(group)
    used_groups.append(group)
    used_appetizers.add(group[0])
    used_dessert.add(group[2])


third_event = []
used_appetizers = set()
used_main = set()
for pair in dessert:
    done = False
    while not done:
        group = random_product(appetizers-used_appetizers,main_dish-used_main,{pair})
        if group not in used_groups:
            done = True
    third_event.append(group)
    used_groups.append(group)
    used_appetizers.add(group[0])
    used_main.add(group[1])

print(first_event)
print(second_event)
print(third_event)