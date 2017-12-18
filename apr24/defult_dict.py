import collections
d = {}

#old style
if 1 in d:
    d[1] += 1
else:
    d[1] = 1

# new style
d = collections.defaultdict(int)
d[1] += 1
d[1] += 1
d[2] += 1
d[1] += 1

print(d)

'''set default'''
d2 = {}
d2.setdefault(1, 0)
print(d2)
d2[1] += 1
print(d2)

'''counter'''
c = collections.Counter('123asdda123ddaaew')
print(c)
print(c.most_common(2))