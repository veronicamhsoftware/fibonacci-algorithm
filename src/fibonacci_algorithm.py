import numpy as np
import time
from matplotlib import pyplot as plt
horizontal_it = []
vertical_it = []
horizontal_rec = []
vertical_rec = []
list_iterative = []
list_recursive = []

def fibRecursive(n):
    if n <= 1:
        return 1
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)


def fibList(n):   
    n_array = np.arange(0,n+1)
    n_array[0] = 1
    if n>0:
        n_array[1] = 1    
    for i in n_array[2:n+1]:                
        n_array[i] = n_array[i-1] + n_array[i-2]        
    return n_array[n]


def fibSerie(n, algorithm):
    if algorithm=="iterative":
        horizontal_it.append(n)
    else:
        horizontal_rec.append(n)
    n_array = np.arange(0,n)    
    start = time.time()
    for i in n_array:
        if algorithm=="iterative":
            list_iterative.append(fibList(i))
        else:
            list_recursive.append(fibRecursive(i))
    end = time.time()    
    if algorithm=="iterative":
        vertical_it.append(end - start)
    else:
        vertical_rec.append(end - start) 


fibSerie(3, "iterative")
fibSerie(5, "iterative")
fibSerie(7, "iterative")
fibSerie(10, "iterative")
fibSerie(15, "iterative")
fibSerie(20, "iterative")
fibSerie(25, "iterative")

plt.title("Iterative")
plt.xlabel("n")
plt.ylabel("T(n)")
plt.plot(horizontal_it,vertical_it)
plt.show()

fibSerie(3, "recursive")
fibSerie(5, "recursive")
fibSerie(7, "recursive")
fibSerie(10, "recursive")
fibSerie(15, "recursive")
fibSerie(20, "recursive")
fibSerie(25, "recursive")

plt.title("Recursive")
plt.xlabel("n")
plt.ylabel("T(n)")
plt.plot(horizontal_rec,vertical_rec)
plt.show()
