def count_a(seq):
    """ Counting the number of As in the sequence """

    result = 0
    for letter in seq:
        if letter == 'A':
            result += 1

    return result

dna = input("Please enter the sequence:")
numberA = count_a(dna)
print ('The number of As is: {}'.format (numberA))

"""Calculate the total sequence length"""
totalLength = len(dna)

"""" Calculate the porcentage """
if totalLength > 0:
    perc = round (100.0 * numberA/totalLength , 1)
else:
    perc = 0

print ("The total length is: {}". format (perc))