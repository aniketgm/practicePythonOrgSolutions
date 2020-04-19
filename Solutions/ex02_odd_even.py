# Ask the user a number and 
# check for even or odd.

import sys
from sys import argv

def printUsage():
    print("")
    print("This program perform three operations:")
    print("1. Check if numbers are even or odd")
    print("2. Check if arg1 is divisible by 4")
    print("3. Check if arg1 is divided by arg2")
    print("")

try:
    script, num1, num2 = argv
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("")
    print("Pass 2 integer arguments ...")
    printUsage()
    sys.exit(1)

printUsage()
print("\n1: ")
if (num1 % 2) == 0:
    print("   First argument is even")
else:
    print("   First argument is odd")

if (num2 % 2) == 0:
    print("   Second argument is even")
else:
    print("   Second argument is odd")

if num1 % 4 == 0:
    print("\n2:", "First argument is divided by 4")
else:
    print("\n2:", "First argument is not divided by 4")

if num1 % num2 == 0:
    print("\n3:", "First argument is divided by Second argument")
else:
    print("\n3:", "First argument not is divided by Second argument")

print("\nHave a good day!")

