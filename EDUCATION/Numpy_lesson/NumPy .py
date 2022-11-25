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
#print(np.uint8(-456))
'Array (n-dimensional array)'
#arr = np.array([1, 2, 3, 4, 5])
#print(type(arr))
#print(arr.dtype) #data type in array
'explicitly specify the data type in the array'
#arr = np.array([1, 2, 3, 4, 5], dtype=np.int8)
#print(arr.dtype)
'change explicitly specify the data type in the array'
#arr = np.array([1, 2, 3, 4, 5], dtype=np.int8)
#arr = np.float16 (arr)
#print(arr)
'Узнать размерность массива можно с помощью .ndim'
#arr = np.array([1, 2, 3, 4, 5])
#print(arr.ndim)
'Узнать общее число элементов в массиве можно с помощью .size'
#arr = np.array([1, 2, 3, 4, 5])
#print(arr.size)
'Форма или структура массива хранится в атрибуте .shape'
#arr = np.array([1, 2, 3, 4, 5])
#print(arr.shape)
'сколько «весит» каждый элемент массива в байтах позволяет .itemsize'
#arr = np.array([1, 2, 3, 4, 5])
#print(arr.itemsize)
'функцией np.zeros создает пустой массив'
#zeros_1d = np.zeros(5)
#zeros_3d = np.zeros((5,4,3), dtype=np.float32)
#print(zeros_3d.shape)
#print(zeros_1d)
'Ещё одной удобной функцией для создания одномерных массивов является arange'
#m = np.arange(5)
#n= np.arange(2.5, 5)
#b = np.arange(2.5, 5, 0.5)
#c = np.arange(2.5, 5, 0.5, dtype=np.float16)
#print(m, n, b, c)
'для работы с дробными параметрами start, stop и step лучше использовать функцию linspace: np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)'
#g = arr = np.linspace(1, 2, 10)
#t = arr = np.linspace(1, 2, 10, endpoint=False)
#step = np.linspace(1, 2, 10, endpoint=True, retstep=True)
#step = np.linspace(1, 2, 10, endpoint=False, retstep=True)
#print(g)

n = np.linspace(-6,21, 60, endpoint = False,retstep = True, dtype = np.float16)
print(n)



