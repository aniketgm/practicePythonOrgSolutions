# Password generator

import string
import random

def main():
    ch = int(input("How much password size you wish? : "))
    allAscii = string.printable[0:-6]
    onlyAlpha = string.ascii_letters
    someStr = ""
    print(someStr.join(random.sample(onlyAlpha, ch)) if (ch <= 8) else someStr.join(random.sample(allAscii, ch)))

if __name__ == '__main__':
    main()
