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


def calculate_gc(seq):
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

def find_kmer(seq, kmer):
    if seq.find(kmer) == -1:
        print "No K-mer found here!"
    else:
        print "Found your K-mer!"
        print




with open('mixed_alphabet.fasta') as fp:
    for name, seq in read_fasta(fp):
        print(name, seq)
        calculate_gc(seq)
        kmer = "AT"
        find_kmer(seq, kmer)


