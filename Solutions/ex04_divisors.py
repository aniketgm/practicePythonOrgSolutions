# Ask user a number and list all the divisor of it.

print("")
print("This script will print all the divisors of an integer supplied by user")
print("")

number = int(eval(input("Enter an integer (> 2): ")))

halfOfNum = int(number / 2)
divisors = [i for i in range(1, halfOfNum+1) if (number % i == 0)]
divisors.append(number)

print("Divisors of %s are : %s" % (number, divisors))

