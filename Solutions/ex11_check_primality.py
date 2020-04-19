# Primality :: Ask a number from user and check if it's a prime number or not

print("")
print(" This script checks for primality of a number")
print("")

def isPrime(num):
    halfOfNum = int(num/2)
    divisors = [i for i in range(1, halfOfNum+1) if (num % i == 0)]
    if len(divisors) == 1:
        return True
    return False

num = int(input(" Enter a number (> 2): "))
print(" It's a prime number") if isPrime(num) else print(" Not a prime number")

