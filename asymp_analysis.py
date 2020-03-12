#Kent Brianne R. Laurente
#BSCS - II
#2018-2063
'''
Algo:

	1. Set n as equal to 1
	2. Ask for input for x which is the limiter of the incrementation of n
	3. Set the condition that while n is less than x n will increment
	4. Append the values of n to a specified list for the graphing
	5. Set the equation to solve itself and directly append to a specified list
		for the graphing
	6. Set the values of 'n' as the x-value and the result of the equations as the 
		y-value values for the graphing 


'''

import math
import time
import matplotlib.pyplot as plt

logar = []
slinear = []
linear = []
quadra = []
poly = []
expo = []

nValue = []

def func():

	n = 1
	x = int(input("Enter limit value of 'n': "))
	
	while n<x:

		nValue.append(n)


#=====================================================#
		#logarithmic	
		logar.append(math.log(n,10))
		print(math.log(n,10))

#=====================================================#
		#s
		slinear.append(n*math.log(n,10))
		print(n*math.log(n,10))

#=====================================================#

		linear.append(n)
		print(n)

#=====================================================#
	
		quadra.append(n**2)
		print(n**2)

#=====================================================#

		poly.append(n**3)
		print(n**3)

#=====================================================#

		expo.append(2**n)
		print(2**n)

#=====================================================#		

		n+=1
func()

plt.plot(nValue,logar)
plt.plot(nValue,slinear)
plt.plot(nValue,linear)
plt.plot(nValue,quadra)
plt.plot(nValue,poly)
plt.plot(nValue,expo)

plt.xlabel("Value of N")
plt.ylabel("Answers")
plt.title("Asymptotic Analysis")
plt.show()
