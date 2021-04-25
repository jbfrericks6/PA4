
#!/usr/bin/env python

from operator import itemgetter
import sys
import csv

#current_word = None
#current_count = 0
#word = None
#avgDiff = 0
#systemCount = 0
buildings = {}
buildingsWTime = {}
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py

    #word, count = line.split('\t', 1)
    time, actualTemp, buildingID = line.split('\t')
    # convert count (currently a string) to int


    try:
        #count = int(count)
        actualTemp = float(actualTemp)
        
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    #if systems already contains a key for the system then append the difference in temp
    #else create the list for the key and then add the difference
    t = 0
    if len(time) == 8:
        t = int(time[0:2])
    else:
        t = int(time[0:1])

    if t >= 9 and t <=17:
        l = [t, actualTemp]
        if buildingID in buildings:
            buildings[buildingID].append(actualTemp)
            #systems[systemID].append(abs(targetTemp - actualTemp))
        else:
            buildings[buildingID] = []
            buildings[buildingID].append(actualTemp)
            #systems[systemID] = []
            #systems[systemID].append(abs(targetTemp - actualTemp))
        if buildingID in buildingsWTime:
            buildingsWTime[buildingID].append(l)
            #systems[systemID].append(abs(targetTemp - actualTemp))
        else:
            buildingsWTime[buildingID] = []
            buildingsWTime[buildingID].append(l)
            
for b in buildings.keys():
    
    avgTemp = sum(buildings[b]) / len(buildings[b])
    #print(buildings[b][1])
    print '%s\t%f' % (b, avgTemp)#, sum(buildings[b]), len(buildings[b]))

hotcsv = 'hot.csv'
try:
    with open(hotcsv, 'w') as csvfile:
        for key in buildingsWTime.keys():
            csvfile.write('%s' % (key))
            for b in buildingsWTime[key]:
                csvfile.write('%s' % (b))
except IOError:
        print("I/O error")
print()
print('building 19')    
print(buildingsWTime['19'])
print()
print('building 2')
print(buildingsWTime['2'])
print()
print('building 7 ')
print(buildingsWTime['7'])
    
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
