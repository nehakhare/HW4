#!/usr/bin/env python
"""mapper.py"""

try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO
    
import csv
import sys

# input comes from standard input
for line in sys.stdin:
    line = line.strip()
    f = StringIO(line)
    words = csv.reader(f, skipinitialspace=True, delimiter=',')
    # remove leading and trailing whitespace
    #line = line.strip()
    #words = list(csv.reader(line, skipinitialspace=True))
    # split the line into words
    #words = line.split()
    # increase counter
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, 
        
        word = word[-5:]
        for letter in word:
            if(letter not in (None,"")):
                print '%s\t%s' % (letter.upper(), 1)
