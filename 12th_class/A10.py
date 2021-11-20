# Write a Python program to plot the function y = x ^ 2
# using the pyplot or matplotlib libraries.

import matplotlib.pyplot as pyplt

def f(x):
    return x ** 2

x = [0,1,2,3,4,5]
y = []
for i in x:
    y.append(f(i))

pyplt.plot(x,y)
pyplt.show()