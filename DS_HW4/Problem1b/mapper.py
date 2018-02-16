#!/usr/bin/env python

import sys
import re

def palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = re.sub('\W+', ' ', line)
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
	if palindrome(word):
	        print '%s\t%s' % (word, 1)
