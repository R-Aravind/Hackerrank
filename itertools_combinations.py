
from itertools import combinations
s =input().split()

for i in range(1,(int(s[1])+1)):
    for j in (list(combinations(sorted(s[0]),i))):
        print(''.join(j))
            

