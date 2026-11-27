
'''1. Implement a function for basic matrix multiplication. It should take two NumPy arrays as inputs and if the dimensions are correct 
it should return the result of the matrix multiplication. Otherwise it should return a message indicating the problem.'''

import numpy as np

def matmult(a1,a2):
    if a1.shape[1] != a2.shape[0]:
        return "Incorrect shape"
    result = np.zeros((a1.shape[0],a2.shape[1]))
    for i in range(a1.shape[0]):
        for j in range(a2.shape[1]):
            result[i,j]= (np.sum(a1[i,:]* a2[:,j]))
    return result



'''2. Create two lists of random numbers, and write a function to add these lists together element wise.
 Convert your lists to NumPy arrays and write a second function that adds these together using NumPy. 
 Time both of your functions and look at the performance difference with inputs of different sizes'''
import random
random.seed(0)
list1 = random.sample(range(0,1000),200)
list2 = random.sample(range(200,5000),200)

def listadd(L1,L2):
    total = []
    if len(L1) > len(L2):
        maxlen = len(L2)
    else:
        maxlen = len(L1)
    for i in range(maxlen):
        total.append(L1[i] + L2[i])
    return total

A1= np.array(list1)
A2=np.array(list2)

def listaddition(A1,A2):
    return A1+A2

### JUPYTER EXCLUSIVE
%timeit listadd(list1,list2)
%timeit listaddition(list1,list2) #numpy addition is faster

'''3. Create a list of random numbers, and a NumPy array of the same data. Try to sort your list and array using the built-in sort and NumPy sort methods
 Again, time these methods and look at how the performance varies over various input sizes. '''

random.seed(1)
sizes = [10, 100, 1000, 10000, 100000,1000000]
list_times = []
numpy_times=[]
for i in sizes:
    randlist = random.sample(range(0,i*10),i)
    rarray = np.array(randlist)
 
#we have to copy it to make it fair, because list.sort sorts it permanently so obviously the next several loops will be very fast
    list_result = %timeit -o x= randlist.copy(); x.sort()
    numpy_result = %timeit -o np.sort(rarray.copy())
    list_times.append(list_result.best)
    numpy_times.append(numpy_result.best)

    '''124 ns ± 0.305 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
    887 ns ± 2.27 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
    2.07 μs ± 2.58 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
    1.04 μs ± 2.03 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
    31.9 μs ± 84.6 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
    12.9 μs ± 10.2 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
    996 μs ± 1.04 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    244 μs ± 28.8 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    15.8 ms ± 27.4 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    3.63 ms ± 8.77 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    204 ms ± 858 μs per loop (mean ± std. dev. of 7 runs, 1 loop each)
    49.2 ms ± 32.2 μs per loop (mean ± std. dev. of 7 runs, 10 loops each)'''


'''4. Using the data you gather from the question above, try to draw some graphs. '''

import matplotlib.pyplot as plt
plt.plot(sizes,list_times, marker = ">", label="Python List")
plt.plot(sizes, numpy_times, marker="o", label="Numpy Array")
plt.legend()
plt.ylabel("time in seconds")
plt.xlabel("list/array size")
plt.show()



'''5. In the data folder is a file called `datafile.txt`. Try to combine all of the skills you've learnt in the previous topics by reading in this data file, 
saving the data into lists, and then converting into NumPy arrays. Plot the data using matplotlib and save your plot.  '''
####
x=[]
y=[]
infile = open("data/datafile.txt") 
for line in infile:
    nums = line.split("\t")
    x.append(float(nums[0]))
    y.append(float(nums[1]))
infile.close()

x_array = np.array(x)
y_array = np.array(y)

plt.plot(x,y,"-x")
fig = plt.figure()
fig.savefig('datafile.png')
