#!/usr/bin/python

from multiprocessing import Pool
from nose.plugins.skip import SkipTest

########################################################################

# This shows the basic call for nosetests

def this_is_a_function():
    # This is the function I want to test
    assert(True)
    
def test_this_is_a_function():
    # This is where I will test it
    p = Pool()
    r = p.apply_async(this_is_a_function)

########################################################################

# This is how you can skip a test:

def skip_the_function():
    # We want to skip this because we know the test will fail
    assert(1 == 2)

def test_skip_the_function():
    raise SkipTest
    p = Pool()
    r = p.apply_async(skip_the_function)

########################################################################

# This will not work to skip a test.

def this_wont_work():
    raise SkipTest
    assert(1 == 2)

def test_this_wont_work():   
    p = Pool()
    r = p.apply_async(this_wont_work)
