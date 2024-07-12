import numpy as np

array1= np.array([1,2,3,4,5])
print(array1)
print(array1[[0,2,4]])
array1.dtype = float
print(array1)
array2 = np.array([0,1.5,2,3.4],dtype=float)
print(array2)
c = np.array(['a','b','c'])
print(c.dtype)
d = np.array([{1:'hello'},'hi'])
print(d.dtype)
m1 = np.array([[1,2,3],[4,5,6],[7,8,9]]) #multidimentional array
print(m1.shape)
print(m1.ndim)
print(m1.size)
m2 = np.array([[[1,2,3],[4,5,6],[3,4,5]],[[7,8,9],[9,0,1],[5,6,7]],[[1,2,3],[4,5,6],[7,8,9]]])
print(m2.shape)
print(m2.ndim)
print(m2.size)
print(m2)
print(m1[0:2,0:2] , 'this is slicing')
print('Trimed m2')
print(m2[:,0:2,0:2], 'this is m2')
m1[1] = np.array([3,4,5])
print(m1)
m1[2] = 99
print(m1)
#axis 0 - perfomed column wise
#axis 1- performed row wise
print(m1.sum(axis=0),'this is sum of axis 0 which is column')
print(m2)
print('')
print(m2.sum(axis=2),'this is sum of axis two in m2 matrix')
## in three dimentional matrix axis=1 is the column axis 2 is the row axis =0 ?
print('')
print(m2.sum(axis=0),'this is sum of axis 0 in m2 matrix')
print('')
print(m2.sum(axis=1),'this is sum of axis 1 in m2 matrix')
#vectorised operations
a = np.array([1,2,3,4])
print(a+10 , 'sum vectorised operations')
print(a*10,'this is multipliction vectorised operations')
a += 100
print(a)
b = np.arange(4)
print(a+b)
#boolean arrays
print(b[[True,False,False,True]])
#boolean operations
print(b>=2)
print(b[b>=2])#filtering the numer arrays with a condition
# some complex tasks
print((b == 0) | (b%2==0),'task 1')
print(~(b>b.mean())) #the oposite of b>b.mean()
# boolean operations are supported for matrixes too!!
c = np.random.randint(0,100,size=(3,3)) #generate a random 2D array
print(c)
print(c.ndim)
print(c>30)
print(c[c>30])
# dot , cross , transposing matrixes .dot() @ T
l = list(range(10))
print(l)
print(sum([x*2 for x in l]))
d  = np.arange(10)
print(sum([i*2 for i in d]))
#two ways
print((d*2).sum())
print(np.sum(d*2))
print(m1)
m1[2] = 101
print(m1)