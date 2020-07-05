
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

# -------------------------------------------------------------------
# Finds the smallest factorial result relative to the given integer n
#
# Problem #26
#
# Author: Carlos L. Cuenca
# Date: 05/19/2020

def countSumOfTwoRepresentations2(n, l, r):

    count = 0

    for index in range(l, r + 1):

        if(index <= (n - index) and (n - index) <= r): count += 1

    return count

# --------------------------------------------------------
# Calculates the amount of money given by the magical well
# when casting a marble
#
# Problem #27
#
# Author: Carlos L. Cuenca
# Date: 07/5/2020

def magicalWell(a, b, n):
    
    salary = 0
    
    while n > 0:
        
        salary += a*b
        a += 1
        b += 1
        
        n -= 1
        
    return salary   