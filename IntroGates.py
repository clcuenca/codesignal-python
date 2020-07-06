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
