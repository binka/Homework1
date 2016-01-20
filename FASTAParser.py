__author__ = "Lincoln Samelson"
__email__ = "lincoln.samelson@colorado.edu"

from decimal import *
import getopt, sys


def Usage():
    # Here is where you print the usage of this application
    print "\nApplication: %s\n%s [options] -f <filename> -c <chromo name> -k <k-mer>     \n" \
          "     To illustrate the how to parse the command line    \n\n" \
          "     -f              - specify filename          \n" \
          "     -c              - specify chromosome name           \n" \
          "     -k              - specifies k-mer to search for  \n" \
          "\n" % (sys.argv[0], sys.argv[0])


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
    gc_content = Decimal((C + G) / total)
    print
    print "%.3f percent GC " % (gc_content)
    print

def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

print(find_str("Happy birthday", "py"))



def find_kmer(seq, kmer):
    if seq.find(kmer) == -1:
        print "No K-mer found here!"
    else:
        print "Found your K-mer!"
        print


with open('small_seq_1000.fasta') as fp:
    for name, seq in read_fasta(fp):
        print(name, seq)
        calculate_gc(seq)
        kmer = "AT"
        find_kmer(seq, kmer)
