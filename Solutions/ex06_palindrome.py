# Ask user a string and check if it's palindrome or not

import sys

print("")
print(" This script checks if the passed string is palindrome or not")
print("")

myStr = input(" Enter a string: ")
print("")

# Here I admit that I looked at other people solution and
# with a little bit of more research and modification I have came up with below one liner.
print("", myStr, "is a palindrome!") if (myStr.lower() == myStr[::-1].lower()) else print("", myStr, "is not a palindrome!")

# My initial solution is this : Logic is to check letters from either end upto the center.
# But obviously there is a more simpler way to do that (as above).
sLen = len(myStr)
fromLeft  = range(0, int(sLen/2), 1)
fromRight = range(sLen-1, int(sLen/2)-1, -1)
for i, j in zip(fromLeft, fromRight):
    if not (myStr[i] == myStr[j]):
        print("", myStr, "is not a palindrome!")
        sys.exit()
print("", myStr, "is a palindrome!")
