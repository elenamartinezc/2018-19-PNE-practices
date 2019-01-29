with open ('CPLX2.txt','r') as f:
    seq = f.read().partition('\n')
    seq1 = seq[2].replace ('\n','')
    countera = 0
    counterg = 0
    counterc = 0
    countert = 0
    for element in seq1:
        if element == 'A':
            countera += 1
        elif element == 'C':
            counterc += 1
        elif element == 'G':
            counterg += 1
        elif element == 'T':
            countert += 1

    print("Number of A:", countera)
    print("Number of C:", counterc)
    print("Number of G:", counterg)
    print("Number of T:", countert)