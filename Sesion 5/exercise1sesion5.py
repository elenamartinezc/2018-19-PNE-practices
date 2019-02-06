def count_bases(seq):
    """ Counting the number of bases in the sequence """

    countera = 0
    counterc = 0
    counterg = 0
    countert = 0
    for letter in seq:
        if letter == 'A':
            countera += 1
        elif letter == 'C':
            counterc += 1
        elif letter == 'G':
            counterg += 1
        elif letter == 'T':
            countert  += 1
    instances = {'A': countera, 'C': counterc, 'G': counterg, 'T': countert}

    return instances

"""We ask the user to enter a sequence"""
seq = input("Please enter the sequence:")
seq = seq.upper()

"""We calculate the length and the percentage"""
length = len(seq)
for keys in count_bases(seq).keys():+
    if length > 0:
        percentage = round(100.0*count_bases(seq)[keys]/length, 1)
        print('This sequence is', length, 'bases in length', '\n')
        print('Base ',keys, '\n', 'Counter: {}'.format(count_bases(seq)[keys]))
        print('Percentage: {}'.format(percentage), '%')




