from collections import Counter

x=int(input())
shoes=dict(Counter(list(map(int,input().split()))))
c=int(input())
s=0
for i in range(c):
    size,price =list(map(int,input().split))
    if shoes[size]:
        s=s+price
        shoes[size]=shoes[size]-1

print(s)

