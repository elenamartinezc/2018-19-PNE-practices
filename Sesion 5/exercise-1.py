def counting(seq):
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
    instances = {'A': countera, 'C': counterc, 'G': counterg, 'T': countert}

    return instances

dna = input("Please enter the sequence:")
counting(dna)

