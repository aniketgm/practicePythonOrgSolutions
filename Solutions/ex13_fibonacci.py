# Ask user the sequence count and print fibonacci sequence

def fibonacci_seq(cnt):
    a = [0, 1]
    for i in range(cnt-1):
        a.append(a[-1] + a[-2])
    return a[1:]

print('')
print(' This script prints fibonacci sequence')
print('')
seq_cnt = int(input(" How long do you want the fibonacci sequence? Enter count: "))
print("", fibonacci_seq(seq_cnt))

