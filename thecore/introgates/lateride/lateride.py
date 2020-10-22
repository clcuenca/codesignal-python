# Codesignal - The Core - Intro Gates
# Late Ride
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def lateRide(n):

    return (int(n/60/10)) + (int(n/60)%10) + (int(n%60/10)) + (int(n%60%10))


# -------
# Program

for line in sys.stdin:

	stripped = int(line.strip())

	print(str(lateRide(stripped)))