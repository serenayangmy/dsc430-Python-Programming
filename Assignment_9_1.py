#DSC 430: Python Programming - Assignment 0901: Numpy Intro
#Student Name: Serena Yang
#Date: Nov, 17, 2020
#Video Link: https://youtu.be/tv8AE_xfAMg
#I have not given or received any unauthorized assistance on this assignment.

import numpy as np

#Use arange to create a NumPy array with 100 equally spaced values in the range 0 through 100 
#(not including 100). Name this NumPy array a.
a = np.arange(100)
print(a)

#Use arange to create a NumPy array with 10 equally spaced values in the range 0 through 100 
#(not including 100). Name this NumPy array b.
b = np.arange(0,100,10)
print(b)

#Use linspace to create a NumPy array in the range 0 through 10 
#(inclusive) with values spaced at 0.1. Call this NumPy array c
c = np.linspace(0.,10., 101)
print(c)

#Create a random two-dimensional array with the dimensions 10 by 10. 
#Call this NumPy array d
d = np.random.random((10,10))

#Reshape a so that it is a two-dimensional array with the dimensions 10 by 10.
a = a.reshape(10,10)

#print results
print("the results of a[4,5]: " + str(a[4,5]))
print("the results of a[4]: " + str(a[4]))
print("the sum of d：" + str(d.sum()))
print("the max of a: " + str(a.max()))
print("the transpose of b: " + str(b.transpose()))
print("the results of adding a and d: \n" + str(a+d))
print("the results of multiplying a and d: \n" + str(a*d))
print("the results of computing the dot product of a and d: \n" + str(np.dot(a,d)))




