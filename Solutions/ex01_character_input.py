# Ask the user their name and age
# and return the year when they will turn 100.

from datetime import date

def printYearHundred(name, age):
    print("")
    age_year = int(date.today().year + (100 - age))
    print(" Hey %s, you will turn 100 in the year %s-%s" % (name, age_year-1, age_year))
    print(" I wish you a good and a healthy life ahead. Cheers!!")
    print("")

print("")
print(" This is a simple program that tells you when you would turn 100 years old!")
name = str(input(" Please enter your name : "))
age  = int(input(" Please enter your age (in years) : "))
printYearHundred(name, age)
print_msg_again = int(input(" Let's print it again. Enter count : "))
for cnt in range(print_msg_again):
    printYearHundred(name, age)

