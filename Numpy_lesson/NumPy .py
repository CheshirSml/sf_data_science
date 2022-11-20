import numpy as np
#a = np.int8(25)
#print(np.iinfo(np.int64))

'overFlow example'
#a = np.int32(2147483610)
#b = np.int32(2147483605)
#print(a, b)
# 2147483610 2147483605
#print(a + b)
'np.float128 not support by MS compiller'
#np.finfo(np.float128)
'full list of numpy commands'
#print(np.sctypeDict)
#print(len(np.sctypeDict))
'all unique commands'
#print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
print(np.uint8(-456))