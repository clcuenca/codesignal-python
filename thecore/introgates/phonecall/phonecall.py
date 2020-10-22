# Codesignal - The Core - Intro Gates
# Phone Call
# Author: Carlos L. Cuenca
# Date:10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def phoneCall(min1, min2_10, min11, s):
    
    if not s or s - min1 < 0: return 0
    
    if s - min1 - 9*min2_10 < 0: 
        
        return int((s - min1) / min2_10 + 1) 
        
    return int((s - min1 - 9*min2_10) / min11) + 10

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")

	values = [int(number) for number in stripped]

	print(str(phoneCall(values[0], values[1], values[2], values[3])))

