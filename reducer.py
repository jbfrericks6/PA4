#!/usr/bin/env python

from operator import itemgetter
import sys

#current_word = None
#current_count = 0
#word = None
#avgDiff = 0
systemCount = 0
systems = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py

    #word, count = line.split('\t', 1)
    targetTemp, actualTemp, systemID = line.split('\t')
    # convert count (currently a string) to int


    try:
        #count = int(count)
        targetTemp = float(targetTemp)
        actualTemp = float(actualTemp)
        #systemID = int(systemID)
        
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    #if systems already contains a key for the system then append the difference in temp
    #else create the list for the key and then add the difference
    if systemID in systems:
        systems[systemID].append(abs(targetTemp - actualTemp))
    else:
        systems[systemID] = []
        systems[systemID].append(abs(targetTemp - actualTemp))
    
for s in systems.keys():
    avgDiff = sum(systems[s]) / len(systems[s])

    print '%s\t%f' % (s, avgDiff)
    
    
    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    

"""
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
"""
