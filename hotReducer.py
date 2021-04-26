
#!/usr/bin/env python

from operator import itemgetter
import sys
import csv

buildings = {}
buildingsWTime = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    time, actualTemp, buildingID = line.split('\t')
    try:
        actualTemp = float(actualTemp)
    except ValueError:
        continue

    #else create the list for the key and then add the difference
    t = 0
    if len(time) == 8:
        t = int(time[0:2])
    else:
        t = int(time[0:1])

    if t >= 9 and t <=17:
        l = [time, actualTemp]
        if buildingID in buildings:
            buildings[buildingID].append(actualTemp)
        else:
            buildings[buildingID] = []
            buildings[buildingID].append(actualTemp)
        if buildingID in buildingsWTime:
            buildingsWTime[buildingID].append(l)
        else:
            buildingsWTime[buildingID] = []
            buildingsWTime[buildingID].append(l)
        
for b in buildings.keys():
    
    avgTemp = sum(buildings[b]) / len(buildings[b])
    print '%s\t%f' % (b, avgTemp)#, sum(buildings[b]), len(buildings[b]))

hotcsv = 'hot.csv'

try:
    with open(hotcsv, 'w') as csvfile:
        writer = csv.writer(csvfile)
        #for b in buildingsWTime.keys():
            #writer.writerows(b)
        for b in buildingsWTime['2']:
            csvfile.write('%s\n' % (b[0]))
        for b in buildingsWTime['2']:
            csvfile.write('%s\n' % (b[1]))
        for b in buildingsWTime['7']:
            csvfile.write('%s\n' % (b[0]))
        for b in buildingsWTime['7']:
            csvfile.write('%s\n' % (b[1]))
        for b in buildingsWTime['19']:
            csvfile.write('%s\n' % (b[0]))
        for b in buildingsWTime['19']:
            csvfile.write('%s\n' % (b[1]))
                        

except IOError:
        print("I/O error")


