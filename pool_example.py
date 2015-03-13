#!/usr/bin/python

import datetime
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
print "List of ids:", vals
print "Parent id:", vals[0]
print "Current id:", vals[1]

