import numpy as np


N,M=list(map(int,input().split()))

a=np.array([list(map(int,input().split())) for i in range(N)])
b=np.array([list(map(int,input().split())) for i in range(N)])

print("{}\n{}\n{}".format(a+b,a-b,a*b))
print(np.divide(a,b).astype('int'))
print('{}\n{}'.format(a%b,a**b))


