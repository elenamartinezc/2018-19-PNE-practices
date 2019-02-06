from bases import count_bases

"""We ask the user to enter a sequence"""
seq1 = input("Please enter the sequence:")
seq1 = seq1.upper()
seq2 = input("Please enter another sequence:")
seq2 = seq2.upper()

"""We calculate the length and the percentage"""
print ("\nSequence 1")
length1 = len(seq1)
for keys in count_bases(seq1).keys():
    if length1 > 0:
        percentage1 = round(100.0*count_bases(seq1)[keys]/length1, 1)
        print('This sequence is', length1, 'bases in length', '\n')
        print('Base ',keys, '\n', 'Counter: {}'.format(count_bases(seq1)[keys]))
        print('Percentage: {}'.format(percentage1), '%')

print ("\nSequence 2")
length2 = len(seq2)
for keys in count_bases(seq2).keys():
    if length2 > 0:
        percentage2 = round(100.0*count_bases(seq2)[keys]/length2, 1)
        print('This sequence is', length2, 'bases in length', '\n')
        print('Base ',keys, '\n', 'Counter: {}'.format(count_bases(seq2)[keys]))
        print('Percentage: {}'.format(percentage2), '%')

