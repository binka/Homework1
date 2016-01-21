import sys, getopt
from decimal import *



def main(argv):


   inputfile = ''
   chromo_name = ''
   k_mer = ''
   outputfile = ''
   name, seq = None, []
   try:
      opts, arg = getopt.getopt(sys.argv[1:], "f:c:k:",["help"])

   except getopt.GetoptError:
      print 'test.py -f <filename> -c <chromo name> -k <k-mer>'

   for opt, arg in opts:
      if opt == '-f':
          inputfile = arg
          read_file(inputfile)
      elif opt == '-c':
         chromo_name = arg
      elif opt == '-k':
         k_mer = arg

   print
   print '############################################'
   print 'Input file is :', inputfile
   print 'Chromosome name is  :', chromo_name
   print 'K-mer to search is :', k_mer
   print '############################################'



   with open(inputfile) as fp:
      for name, seq in read_file(fp):
         name = name.replace(">", "")
         if name == chromo_name:
            calculate_gc(seq, name)
            find_kmer(seq, k_mer)




def read_file(filename):
   name, seq = '', []
   for line in filename:
      line = line.rstrip()
      if line.startswith(">"):
         if name: yield (name, ''.join(seq))
         name, seq = line, []
      else:
         seq.append(line)

   if name: yield (name, ''.join(seq))
   seq = str(seq)
   name



def calculate_gc(seq, name):
   seq = seq.upper()
   total = len(seq)
   C = seq.count("C")
   C = float(C)
   G = seq.count("G")
   G = float(G)
   A = seq.count("A")
   A = float(A)
   T = seq.count("T")
   T = float(T)
   gc_content = Decimal((C + G) / total) * 100
   print
   print name, " contains %.2f percent GC " % (gc_content)
   print


def find_kmer(seq, kmer):
    print seq.find(kmer)


if __name__ == "__main__":
   main(sys.argv[1:])
