from itertools import groupby
n= input()
print(*[(len(list(v)),int(k)) for k,v in groupby(n)])

