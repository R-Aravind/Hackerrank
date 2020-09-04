import numpy as np
np.set_printoptions(sign=' ')

arr=list(map(float,input().split()))
s=np.array(arr)
print(np.floor(s),np.ceil(s),np.rint(s),sep='\n')





