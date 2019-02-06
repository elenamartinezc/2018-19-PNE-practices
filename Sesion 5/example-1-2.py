from bases import count_bases


"""We ask the user to enter a sequence"""
seq = input("Please enter the sequence:")
seq = seq.upper()

"""We calculate the length and the percentage"""
length = len(seq)
for keys in count_bases(seq).keys():
    if length > 0:
        percentage = round(100.0*count_bases(seq)[keys]/length, 1)
        print('This sequence is', length, 'bases in length', '\n')
        print('Base ',keys, '\n', 'Counter: {}'.format(count_bases(seq)[keys]))
        print('Percentage: {}'.format(percentage), '%')