# Rock-Paper-Scissor game between 2 players

print('')
print(' ### Game of Rock-Paper-Scissor ###')
print(' Choices: rock | paper | scissor')

def isWinner(s1, s2):
    if (s1 == 'paper' and s2 == 'rock') or \
       (s1 == 'scissor' and s2 == 'paper') or \
       (s1 == 'rock' and s2 == 'scissor'):
        return True
    else:
        return False

ans = 'y'
while ans.lower() == 'y':
    print('')
    p1 = input(" Player 1 choice: ")
    p2 = input(" Player 2 choice: ")
    if isWinner(p1.lower(), p2.lower()):
        print(" Player 1 wins this round")
    elif isWinner(p2.lower(), p1.lower()):
        print(" Player 2 wins this round")
    else:
        print(" It's a tie!")
    ans = input(" Next round ? (Y/N): ")

