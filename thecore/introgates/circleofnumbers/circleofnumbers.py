# Codesignal - The Core - Intro Gates
# Circle of Numbers
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def circleOfNumbers(n, firstNumber):
    
    return (firstNumber + int(n / 2)) % n

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")
	array = [int(number) for number in stripped]

	print(str(circleOfNumbers(array[0], array[1])))