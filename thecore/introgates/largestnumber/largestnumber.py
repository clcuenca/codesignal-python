# Codesignal - The Core - Intro Gates
# Largest Number
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def largestNumber(n):

	return 10**n - 1

# -------
# Program

for line in sys.stdin:

	stripped = int(line.strip())

	print(largestNumber(stripped))