from turtle import color
import numpy
import matplotlib.pyplot as plt
x=numpy.arange(-2,2,0.00001)
f1=numpy.sqrt(1-(abs(x)-1)**2)
f2=numpy.arccos(1-abs(x))-numpy.pi
plt.plot(x,f1,color='darkred')
plt.plot(x,f2,color='darkred')
plt.fill(x,f1,color='crimson')
plt.fill(x,f2,color='crimson')
plt.subplots_adjust(0,0,1,1)
plt.show()