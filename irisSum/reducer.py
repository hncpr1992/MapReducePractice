#!/usr/bin/python3
import sys

slenTotal = 0
oldKey = None
   
for line in sys.stdin:
    data = line.strip().split("\t")
    	
    if len(data) != 2:
        continue
    
    currentKey,currentValue = data
    
    if oldKey and oldKey != currentKey:
        print("{0}\t{1}".format(oldKey,slenTotal))
        slenTotal = 0
    
    oldKey = currentKey
    slenTotal += float(currentValue)
print("{0}\t{1}".format(oldKey,slenTotal))
