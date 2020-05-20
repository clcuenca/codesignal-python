
# -------------------------------------------------------------------
# Finds the smallest factorial result relative to the given integer n
#
# Problem #25
#
# Author: Carlos L. Cuenca
# Date: 05/19/2020

def leastFactorial(n):

    factorial = 1
    result = 1

    while result < n:

        factorial += 1
        result *= factorial

    return result

def countSumOfTwoRepresentations2(n, l, r):

    count = 0

    for index in range(l, r):

        if(index <= (n - index) and (n - index) <= r): count += 1

    return count