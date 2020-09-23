n1=int(input())
M=set(map(int,input().split()))
n2=int(input())
N=set(map(int,input().split()))

for x in (sorted(M.symmetric_difference(N))):
    print(x)
