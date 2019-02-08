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
        complementary2 = Seq(complementary)
        return complementary2

    def reverse(self):
        reverse = self.strbases [::-1]
        reverse2 = Seq(reverse)
        return reverse2

    def count(self,base):
        counting = (self.strbases).count(base)
        return counting

    def perc (self, base):
        length = len(self.strbases)
        percentage = round(((self.strbases.count(base))/length) * 100, 1)
        return percentage