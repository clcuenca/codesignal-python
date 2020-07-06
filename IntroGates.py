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