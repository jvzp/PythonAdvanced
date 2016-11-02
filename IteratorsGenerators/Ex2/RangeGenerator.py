#!/usr/bin/env python3

def next_increment(start=0, stop=10):
    while stop:
        stop -= 1
        yield start
        start += 1

def main():
    for i in next_increment(0,10):
        print ("{}".format(i))

if __name__ == "__main__":
    main()
