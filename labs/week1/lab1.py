"""
Andrea Murphy
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 29, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""
import tests

def give_me_a_string():
    """
    This function returns a string value
    """
    message = 'Hello, yall'
    return(message)
    pass

def give_me_an_integer():
    """
    This function returns an integer value
    """
    int = 4
    return(int)
    pass

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    x = 5

    if x == 5:
        return True
    else:
        return False
    pass

def give_me_a_float():
    """
    This function returns a float value
    """
    float= 3.5
    return(float)
    pass

def give_me_a_list():
    """
    This function returns a list
    """
    t =[1,2,3]
    return(t)
    pass

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    d = {cat:1, dog:2}
    return(d)
    pass

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    tup= (555, 'Website', 'Application', 805)
    return tup
    pass

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    runningtotal = 0
    for counter in range(0,10,1)
        runningtotal = runningtotal +1
    return runningtotal
    pass


def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if (num % 2 == 0):
        return True
    else:
        return False
    pass

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    number1=1
    number2=3

    if number1 < number2
        return True
    else
        return False
    pass
