# Codesignal - The Core - Intro Gates
# Max Multiple
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def maxMultiple(divisor, bound):

	return bound - (divisor % divisor)

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")

	array = [int(number) for number in stripped]

	print(maxMultiple(array[0], array[1]))