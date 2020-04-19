# Reverse the order of words in a sentence (not the characters)

def reverseSentence(a):
    return a.split()[::-1]

a = input("Enter some sentence : ")
print("Reverse word order : ", ' '.join(reverseSentence(a)))
