#!/usr/bin/python3

import sys

oldKey = None
highest = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    deptStore,wSales = data   
    currentKey = deptStore.split("+")
    
    if oldKey and oldKey != currentKey:
        print("The highest sales of store {1} in Department {0} is: {2}".format(oldKey[0],oldKey[1],highest))
        oldKey = currentKey
        highest = 0
    
    oldKey = currentKey
    highest = max(float(wSales),highest) 

# print the last key-value pair
print("The highest sales of store {1} in Department {0} is: {2}".format(oldKey[0],oldKey[1],highest))







