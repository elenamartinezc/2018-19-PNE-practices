chain = input("Enter a valid sequence:")
length = len(chain)
print ("The length is", length)
countera = 0
counterg = 0
counterc = 0
countert = 0
for element in chain:
    if element == 'A':
        countera += 1
    elif element == 'C':
        counterc += 1
    elif element == 'G':
        counterg += 1
    elif element == 'T':
        countert += 1

print ("Number of A:", countera)
print ("Number of C:", counterc)
print ("Number of G:", counterg)
print ("Number of T:", countert)
