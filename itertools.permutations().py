from itertools import permutations

S=input().split()


L=list(permutations(S[0],int(S[1])))
for i in L:
    print(''.join(i))
    
