#! /usr/bin/env python

import sys

letter = []
if __name__ == '__main__': 
    for line in sys.stdin:
        #print(line)
        letter.append(line.split())
    for i in letter:
        sys.stdout.write("{}\t{}\t1\n".format(i[0], i[2]))
    pass