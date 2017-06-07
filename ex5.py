import random
a = [random.randrange(10) for n in range(10)]
b = [random.randrange(10) for n in range(10)]

new_list = list(set([x for x in a if x in b]))

print(new_list)
