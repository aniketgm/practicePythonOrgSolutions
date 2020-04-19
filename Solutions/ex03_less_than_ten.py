# List Printing and some operations on it.

print("")
print(" This script contains first 12 fibonacci numbers")
print(" This script prints fibonacci numbers less than 5")
print(" And also prints the fibonacci numbers less than the number provided by user.")
print("")

a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(" Original List : ", a)

print(" List of elements less than 5: ", [b for b in a if (b < 5)])

num = int(input(" Enter a number: "))
print(" List of elements less than %s" % num, [c for c in a if (c < num)])
