from Seq import Seq

seq1 = Seq ("AGTACACTGGT")
seq2 = Seq ("CGTAAC")
seq3 = seq1.complement()
seq4 = seq3.reverse()

print ("Sequence 1: "+seq1.strbases())
print ("Length:{}".format(seq1.len)
print ("Bases count: A: {} C:{} G:{} T: {}".format (seq1.count('A'), seq1.count('C'), seq1.count('G'), seq1.count('T'))
print ("Bases percentage: A: {}% C:{}% G:{}% T:{}%".format (seq1.perc('A'), seq1.perc('C'), seq1.perc('G'), seq1.perc('T'))

print ("Sequence 2: "+seq2.strbases())
print ("Length:{}".format(seq2.len)
print ("Bases count: A: {} C:{} G:{} T: {}".format (seq2.count('A'), seq2.count('C'), seq2.count('G'), seq2.count('T'))
print ("Bases percentage: A: {}% C:{}% G:{}% T:{}%".format (seq2.perc('A'), seq2.perc('C'), seq2.perc('G'), seq2.perc('T'))

print ("Sequence 3: "+seq3.strbases())
print ("Length:{}".format(seq3.len)
print ("Bases count: A: {} C:{} G:{} T: {}".format (seq3.count('A'), seq3.count('C'), seq3.count('G'), seq3.count('T'))
print ("Bases percentage: A: {}% C:{}% G:{}% T:{}%".format (seq3.perc('A'), seq3.perc('C'), seq3.perc('G'), seq3.perc('T'))

print ("Sequence 4: "+seq4.strbases())
print ("Length:{}".format(seq4.len)
print ("Bases count: A: {} C:{} G:{} T: {}".format (seq4.count('A'), seq4.count('C'), seq4.count('G'), seq4.count('T'))
print ("Bases percentage: A: {}% C:{}% G:{}% T:{}%".format (seq4.perc('A'), seq4.perc('C'), seq4.perc('G'), seq4.perc('T'))