from collections import defaultdict

d1 = {1: 2, 3: 4}
d2 = {1: 6, 3: 7}
d3 = {1: 4, 3: 90}
d4 = {1: 78, 3: 44, 85:55}

dd = defaultdict(list)

for d in (d1, d2, d3, d4): # you can list as many input dicts as you want here
    for key, value in d.items():
        dd[key].append(value)

print(dd)
print(type(dd))
b = dict(dd)
print(b)
