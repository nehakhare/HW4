#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

curr_word = None
curr_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently  string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so 
        # ignore this line
        continue

    # this IF-switch  works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if curr_word == word:
        curr_count += count
    else:
        if curr_word:
            # write result to STDOUT
            print '%s\t%s' % (curr_word, curr_count)
        curr_count = count
        curr_word = word

#  output the last word if needed!
if curr_word == word:
    print '%s\t%s' % (curr_word, curr_count)
