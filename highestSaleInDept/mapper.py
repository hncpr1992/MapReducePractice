#!/usr/bin/python3

# The task is to calculate the higest weekly sales within each store of each department
import sys

for line in sys.stdin:
    data = line.strip().split(",")
    store,dept,date,wSales,isHoliday = data
    print("{0}+{1}\t{2}".format(dept,store,wSales))

