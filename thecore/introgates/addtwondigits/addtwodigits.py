# Codesignal - The Core - Intro Gates
# Add Two Digits
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def addTwoDigits(number):

	return (number / 10) + (number % 10)

# -------
# Program

for line in sys.stdin:

	stripped = int(line.strip().split(" "))

	print(str(addTwoDigits(stripped)))