#coding=utf-8
import numpy as np

a = np.array([[2,23,4],[2,32,4]])  # 2d 矩阵 2行3列
print(a)

a = np.zeros((3,4)) # 数据全为0，3行4列
print(a)

a = np.ones((3,4),dtype = np.int)   # 数据为1，3行4列
print(a)

a = np.empty((3,4)) # 数据为empty，3行4列
print (a)

a = np.arange(10,20,2) # 10-19 的数据，2步长
print (a)

a = np.arange(12).reshape((3,4))    # 3行4列，0到11
print (a)

a = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
print (a)

a = np.linspace(1,10,20).reshape((5,4)) # 更改shape
print (a)