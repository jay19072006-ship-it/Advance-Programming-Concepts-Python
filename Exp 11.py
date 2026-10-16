# Numpy 123D
# Pandas series dataframe
# Transpose 2d
# 1D 3D array print
# Add label in arr fun
# Operation on matrix -+/*
# Expo
# .csv

import numpy as np
import pandas as pd

a = np.array([1,2,3,4])
print("\n1D:", a)

b = np.array([[1,2],[3,4]])
print("\n2D:",b)

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("\n3D:",c)

print("\nTranspose of 2D array of a:")
print(a.T)

m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])

print("\nMatrix Addition:\n",m1+m2)

print("\nMatrix Subtraction:\n",m1-m2)

print("\nMatrix Multiplication:\n",m1*m2)

print("\nMatrix Division:\n",m1/m2)

print("\nExponential of 1D array:",np.exp(a))

print("\nPandas Series with labels:")
s = pd.Series([10, 20, 30, 40], index=['A','B','C','D'])
print(s)

print("\nDataFrame example:")
df = pd.DataFrame({'Name':['Viraj','Raj','Rahul'],'Marks':[80,85,70]})
print(df)

csv_file = 'student_data.csv'
print(pd.read_csv(csv_file))