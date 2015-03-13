#!/usr/bin/python

from multiprocessing import Pool
from nose.plugins.skip import SkipTest

########################################################################

# This shows the basic call for nosetests

def this_is_a_function():
    # This is the function I want to test (a == b)
    a = 1
    b = 1
    return [a,b]
    
def test_this_is_a_function():
    # This is where I will test it
    p = Pool()
    r = p.apply_async(this_is_a_function)
    val = r.get()
    assert(val[0] == val[1])

########################################################################

# This is how you can skip a test:

def skip_the_function():
    # We want to skip this because we know the test will fail (a != b)
    a = 1
    b = 2
    return [a,b]

def test_skip_the_function():
    raise SkipTest
    p = Pool()
    r = p.apply_async(skip_the_function)
    val = r.get()
    assert(val[0] == val[1])

########################################################################

# This will also work to skip a test.

def this_also_skips():
    raise SkipTest
    a = 1
    b = 2
    return [a,b]

def test_this_also_skips():   
    p = Pool()
    r = p.apply_async(this_also_skips)
    val = r.get()
    assert(val[0] == val[1])

#######################################################################

# This will return as a pass even though we know it should fail!

def this_will_pass_but_it_shouldnt():
    a = 1
    b = 2
    assert_equal(a,b)
    
def test_this_will_pass_but_it_shouldnt():
    p = Pool()
    r = p.apply_async(this_will_pass_but_it_shouldnt)
