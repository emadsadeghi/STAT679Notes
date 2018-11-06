#!/usr/bin/env python 
"""
This module calculates binomial coefficients of the form C(n,k).

Calculating binomial coefficients is not easy numerically. 
The number of ways to choose k elements among n is C(n,k) = n! / (k! (n-k)!) where factorial n: n! = 1*2*...*n becomes very big very fast. But many terms cancel each other in “n choose k”, and it is a lot easier numerically to calculate the log factorial: 
log(n!) = log(1) + ... + log(n). 

Now, note that we can write log(C(n,k)) = log(n!/k!) - log((n-k)!). Thus, instead of calculating C(n,k) directly (which is numerically inefficient), we can compute the log factorials log(n!/k!) and log((n-k)!) to find log(C(n,k)), which is in turn more efficient. 

Examples Outputs:

$ ./binomial.py -n 150 -k 40
4408904561911885789946649584764715008

$ ./binomial.py -n 1500 -k 400 --log
866.1129352492226

$ ./binomial.py --help
usage: binomial.py [-h] [-n N] [-k K] [-l] [--test]

optional arguments:
  -h, --help  show this help message and exit
  -n N        total number of items to choose from
  -k K        number of items to choose
  -l, --log   returns the log binomial coefficient
  --test      tests the module and quits

$ ./binomial.py --test
testing the module...
done with tests
"""

import sys
import argparse
import math

# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n",metavar='N', type=int, help="total number of items to choose from")
parser.add_argument("-k",metavar='K', type=int, help="number of items to choose")
parser.add_argument("-l", '--log',action="store_true", help="returns the log binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

def logfactorial(n, k=0):
    """ 
    This function calculates log(n!/k!).
    The arguments n and k should be non-negative integers. 

    Returns log(n!) = log(1*...*n) = log(1) + ... + log(n) when k is 0.
    Returns log(n!/k!) = log((k+1)*...*n) = log(k+1) + ... + log(n) when k is not 0.
    Return log(1)=0 if k > n.
    k is optional, 0 by default.

    Examples:

    >>> logfactorial(5,0)
    4.787491742782046
    >>> logfactorial(5,2)
    4.0943445622221
    >>> logfactorial(5,6)
    0
    >>> logfactorial(5,5)
    0
    """
    assert type(n)==int, "n should be an integer."
    assert n >= 0, "n should be positive."
    assert type(k)==int, "k should be an integer."
    assert k >= 0, "k should be positive."

    if (k > n):
        return 0
    else:
        logfactorial_num = 0
        for i in range(k+1, n+1):
            logfactorial_num = logfactorial_num + math.log(i)
    return logfactorial_num

def choose(n, k, log_value=0):
    """
    This function calculates the binomial coefficient C(n,k).
    The arguments n and k should be non-negative integers, and log_value is an optional argument (with 0 as its default value). 

    Returns C(n,k) when log_value = 0.
    Returns log(C(n,k)) when log_value = 1.

    Examples:

    >>> choose(5,3)
    10
    >>> choose(150,40)
    4408904561911885789946649584764715008
    >>> choose(5,0)
    1
    >>> choose(1500,400, log_value=1)
    866.1129352492226
    >>> choose(0,0)
    1
    """
    assert n >= 0, "n should be positive"
    assert k >= 0, "k should be positive"
    assert n >= k, "k should be less than or equal to n"

    if (log_value == 0):
        # convert to integer 
        return round(math.exp(logfactorial(n, k) - logfactorial(n-k)))
    else: 
        return logfactorial(n, k) - logfactorial((n-k))

def runTests():
    print("testing the module...")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print(choose(args.n, args.k, log_value=args.log))
