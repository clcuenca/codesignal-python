# --------------------------------------------
# Returns the sum of the given number's digits
#
# Problem #1
#
# @author: Carlos L. Cuenca
# @date 07/06/2020

def addTwoDigits(n):

	return (n % 10) + int(n / 10)

# ----------------------------------------
# Returns the largest number with n digits
#
# Problem #2
#
# @author: Carlos L. Cuenca
# @date: 07/06/2020

def largestNumber(n):

    value = 0

    for number in range(n):
        
        value = value*10 + 9
        
    return value

# -----------------------------------------------------------------------
# Returns the amount of candies each individual child will be able to eat
# from a pot containing m candies
#
# Problem #3
# 
# @author Carlos L. Cuenca
# @date: 07/06/2020

def candies(n, m):
    
    return n * int(m / n)

# ----------------------------------------------------------------------------
# Returns the amount of seats that will be blocked if the person were to leave
#
# Problem #4
#
# @author: Carlos L. Cuenca
# @date: 07/06/2020

def seatsInTheater(nCols, nRows, col, row):
    
    return (nCols - col + 1)*(nRows - row)

# -----------------------------------------------------------------------
# Returns the largest number that's divisible by the given divisor & less
# than or equal to the given bound
#
# Problem #5
# 
# @author: Carlos L. Cuenca
# @since: 07/06/2020

def maxMultiple(divisor, bound):

	return bound - (divisor % divisor)

# -----------------------------------------------------------------------------
# Returns the radially opposite number from the given amount of numbers
# and the given first number. Since the numbers are in a circle, 'overflowing'
# numbers need to be taken into account (e.g. 7 + 5 with a given n = 10 
# should equate to 2, not 12) therefore, the remainder is taken; this also
# covers the case when the radially opposite number is less that a given n = 10
#
# Problem #6
#
# @author: Carlos L. Cuenca
# @since: 07/06/2020

def circleOfNumbers(n, firstNumber):
    
    return (firstNumber + int(n / 2)) % n

# ------------------------------------------------------------------------
# Returns the sum of each of the digits after n minutes have elapsed since
# 00:00.
#
# Problem #7
#
# @author: Carlos L. Cuenca
# @since: 07/06/2020

def lateRide(n):

    return (int(n/60/10)) + (int(n/60)%10) + (int(n%60/10)) + (int(n%60%10))

# --------------------------------------------------------------------------
# Returns the amount of minutes given s cents and min1, min2_10, min11 rates
# for the first minute, second to tenth, & eleventh or above minutes
#
# Problem #8
# 
# @author: Carlos L. Cuenca
# @since: 07/06/2020

def phoneCall(min1, min2_10, min11, s):
    
    if not s or s - min1 < 0: return 0
    
    if s < min1 + 9*min2_10: 
        
        return int((s - min1) / min2_10 + 1) 
        
    return int((s - min1 - 9*min2_10) / min11) + 10
