class Seq():
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        complementary = ''
        for base in self.strbases:
            base = base.upper()
            if base == 'A':
                complementary += 'T'
            elif base == 'T':
                complementary += 'A'
            elif base == 'C':
                complementary += 'G'
            elif base == 'G':
                complementary += 'C'
        return complementary

    def reverse(self):
        return

    def count(self,base):
        counting = (self.strbases).count(base)


    def perc (self, base):




