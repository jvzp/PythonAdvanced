#!/usr/bin/env python

with open("file.txt", "r") as f:
    for line_number,line in enumerate(f):
        temp = line.rstrip('\n')
        numbers = temp.split(",")
        for column,x in enumerate(numbers):
            if not x.isdigit():
                print "No digit on line: {} in column: {}, character is: {}".format(line_number, column, x)

