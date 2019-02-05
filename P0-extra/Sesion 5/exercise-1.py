def count_a(seq):
    """ Counting the number of As in the sequence """

    countera = 0
    counterc = 0
    counterg = 0
    countert = 0
    for letter in seq:
        if letter == 'A':
            countera += 1
        elif letter == 'C':
            counterc += 1
        elif counterg == 'G':
            counterg += 1
        elif countert == 'T':
            countert  += 1

    return countera,counterc,counterg,countert

dna = input("Please enter the sequence:")
numberA = countera(dna)
numberC = counterc(dna)
numberG = counterg(dna)
numberT = countert(dna)
print ('The number of As is: {}'.format (numberA))
print ('The number of Cs is: {}'.format (numberC))
print ('The number of Gs is: {}'.format (numberG))
print ('The number of Ts is: {}'.format (numberT))

"""Calculate the total sequence length"""
totalLength = len(dna)

"""" Calculate the porcentage """
if totalLength > 0:
    perc = round (100.0 * numberA/totalLength , 1)
else:
    perc = 0

print ("The total length is: {}". format (perc))