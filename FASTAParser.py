__author__ = "Lincoln Samelson"
__email__ = "lincoln.samelson@colorado.edu"

from decimal import *

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

with open('mixed_alphabet.fasta') as fp:
    for name, seq in read_fasta(fp):
        print(name, seq)
        total = len(seq)
        total = float(total)
        C = seq.count("C")
        C = float(C)
        G = seq.count("G")
        G = float(G)
        A = seq.count("A")
        A = float(A)
        T = seq.count("T")
        T = float(T)

        gc_content = Decimal((C+G)/total)
        print
        print "%.3f percent GC " % (gc_content)
        print