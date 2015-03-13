#!/usr/bin/python

import os

from multiprocessing import Pool

########################################################################

# The most basic use is to apply a function on a single process with no 
# return values

def get_id_print():
    # This function gets the parent process id (pp) and the current
    # process id (p).
    
    pp = os.getppid()   # parent
    p = os.getpid()     # current
    
    print "parent process:", pp
    print "current process:", p
    
p1 = Pool()
r1 = p1.apply_async(get_id_print)

########################################################################

# Here we use the same function but with return values

def get_id_return():
    # This function will return the values
    
    pp = os.getppid()   # parent
    p = os.getpid()     # current
    
    return [pp, p]
    
p2 = Pool()
r2 = p2.apply_async(get_id_return)
vals = r2.get()
print "\nList of ids:", vals
print "Parent id:", vals[0]
print "Current id:", vals[1]

########################################################################

# Here we demonstrate how to submit a value to a function and call it 
# once or map it many times.

def f(x):
    r = x*2
    return r

# submitting a single value
p3 = Pool()
r3 = p3.apply_async(f, [3]) 
v = r3.get()
print "\n", v

# submitting many values with map()
p4 = Pool()
r4 = p4.map(f, [1,2,3]) 
print "\n", r4

# Showing that map still stays on separate processes
def get_id_val(v):
    
    pp = os.getppid()   # parent
    p = os.getpid()     # current
    
    return [pp, p]
    
p5 = Pool()
r5 = p5.map(get_id_val, [1,1,1])
print "\n", r5
