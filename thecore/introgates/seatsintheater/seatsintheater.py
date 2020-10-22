# Codesignal - The Core - Intro Gates
# Seats in Theater
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def seatsInTheater(nCols, nRows, col, row):
    
    return (nCols - col + 1)*(nRows - row)

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")
	array = [int(number) for number in stripped]

	print(str(seatsInTheater(array[0], array[1], array[2], array[3])))