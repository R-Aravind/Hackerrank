input().split()
a=input().split()
A,B= set(input().split()),set(input().split())

print(sum([1 if i in A else -1 if i in B else 0 for i in a]))



