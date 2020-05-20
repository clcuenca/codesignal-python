
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
