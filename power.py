import os
import numpy as np
import sys


f=float(sys.argv[1])

def power(x):
    return x**2

def square_root(x):
    return np.sqrt(x)

square=power(f)
root=square_root(f)

print "square result=",square, "root result=",root

