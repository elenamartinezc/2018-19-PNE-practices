class Seq:
    """A class for representing sequences"""
    def __init__(self,strbases):
        print("New empty object")
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

s1 = Seq('ATGTGATCATGACA')
s2 = Seq ('ATCTGTCATG')

l1 = s1.len()
l2 = s2.len()

print("Sequence 1: {}".format(s1))
print("Sequence 2: {}".format(s2))
print ("The length of sequence 1: {}".format(l1))
print ("The length of sequence 2: {}".format(l2))