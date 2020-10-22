# Codesignal - The Core - Intro Gates
# Candies
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def candies(n, m):

	return n*int(m/n)

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")

	array = [int(number) for number in stripped]

	print(str(candies(array[0], array[1])))