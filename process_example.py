#!/usr/bin/python

import os

from multiprocessing import Process

########################################################################

# First let's get the process id for just running this script

current = os.getpid()
print "\nCurrent process:", current

########################################################################

# Now let's launch another process and get the id.

def get_id():
    # This function gets the parent process id (pp) and the current
    # process id (p).
    
    pp = os.getppid()
    p = os.getpid()
    
    print "parent process:", pp
    print "current process:", p


# Let's call the function get_id twice. The parent process should
# have the same id in both cases but the current processes will have 
# different ids.

print "\nFirst call:"
p1 = Process(target=get_id)
p1.start()
p1.join()

print "\nSecond call:"
p2 = Process(target=get_id)
p2.start()
p2.join()    


# Now let's demonstrate what happens if we call a process and start it
# but forget to join it to the parent process before starting a new one.

print "\nThis is what happens if we join() at the end:"

print "\nFirst call:"
p3 = Process(target=get_id)
p3.start()

print "\nSecond call:"
p4 = Process(target=get_id)
p4.start()
p4.join()

