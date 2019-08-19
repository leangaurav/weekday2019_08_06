#1- create a numpy array of 5 zeros.
  #- check datatype, itemsize and shape of above
import numpy as np
z = np.zeros(5)
print(z, z.dtype, z.itemsize, z.shape)

#2- create a numpy array of ones of shape (5,4)
o = np.ones([5,4])
print(o)

#3- create a matrix of shape 4,5 with numbers from 1-20
val = np.arange(1,21)
val.resize(5,4)
print(val)

#4- multiply all elements of above array by 10
new_val = val*10
print(new_val)
#5- print odd elements from array
print(new_val[new_val%2==0])
#6- replace all even elements by their negative
print(-new_val[new_val%2==0])


#7- create a linearly spaced matrix M1 of size 4x4 having values in range 1-16
M1 = np.arange(1,17)
M1.resize(4,4)
#8- create a transpose of above matrix call it M2
M2 = M1.T
#9- find sum of above matrix M3 = (M1 + M2)
M3 = (M1 + M2)
MT1 = M3.T
#10- Find Transpose of M3, Call it MT1. Check if M3 == MT1
print(M3 == MT1)
#11- find diffrence of M4 = (M1 - M2)
M4 = (M1 - M2)

#12- Find Transpose of M4, Call it MT2. Check if M4 == MT2. Also check if M4 == -MT2
MT2 = M4.T
print(M4==-MT2)

#13- create a matrix (3x4) R1 of random numbers between 10-40
R1 = np.random.randint(10,40,12)
R1.resize(3,4)
print(R1)
#14- find min and max column wise
maxi = np.max(R1, axis=1)
print('max',maxi)
mini = np.min(R1, axis=1)
print('min',mini)
sum_all = np.sum(R1, axis=1)
print('sum_all',sum_all)
#15- replace the last column with sum of all the columns
R1[:,3] = sum_all
print(R1)
#16- create a matrix (3x4) R1 of random numbers between 10-40
R1 = np.random.randint(10,40,12)
#17- replace all even elements with nan in R1
R1.resize(3,4)
print(R1)
x = np.where(R1%2==0,np.nan,R1)
print(x)