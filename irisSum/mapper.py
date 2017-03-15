#!/usr/bin/python3
import sys

for line in sys.stdin:
    data = line.strip().split(",")
    
    # empty rows
    if len(data) != 5:
        continue

    slen,swid,plen,pwid,species = data
    print("{0}\t{1}".format(species,slen))
