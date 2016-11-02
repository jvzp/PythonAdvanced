#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(description="Merges to files to one unique file, run with ./Uniquefy file1.txt, file2.txt, result.txt")
parser.add_argument("inputfiles", type=str, nargs='+', help="multiple files")
parser.add_argument("-of", "--output_file", type=str, help="Select an output file for the result")
parser.add_argument("-op", "--operation", type=str, required=True, help="unique, intersection or difference")
args = parser.parse_args()

lijst = []

if args.operation == "unique":
    for x in args.inputfiles:
        if not os.path.isfile(x):
            print "file: {} does not exist".format(x)
            continue
        with open(x, "r") as f1:
            for line in f1:
                temp = int(line.rstrip('\n'))
                lijst.append(temp)
elif args.operation == "intersection":
    print "operation not supported yet..."
elif args.operation == "difference":
    print "operation not supported yet..."
else:
    print "Unsupported operation..."

set1 = set(lijst)

of = open(args.output_file, "w")
for el in set1:
    of.write("{}\n".format(el))
of.close()
