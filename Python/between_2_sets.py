#You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

#The elements of the first array are all factors of the integer being considered
#The integer being considered is a factor of all elements of the second array

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def gcd(lst):
    x=reduce(math.gcd,lst)
    return x

def lcm(a,b):
    return a*b//gcd([a,b])

def find_lcm(lst):
    return reduce(lcm,lst)

def getTotalX(a, b):
    count=0
    X=find_lcm(a)
    Y=gcd(b)
    for i in range(X,Y+1,X):
        if(Y%i==0):
            count=count+1
    return count

    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
