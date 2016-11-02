#!/usr/bin/env python

def trace(func):
    def traced(*args, **kwargs):
        print("/***********************************************************")
        print(" * Trace: {0} ({1}:{2})"
              .format(func.__name__, func.__code__.co_filename, func.__code__.co_firstlineno))
        print(" * Function called with:")
        for number,arg in enumerate(args):
            print(" * argument {0}: {1}".format(number,arg))
        print(" ***********************************************************/")
        print("")
        return func(*args, **kwargs)
    return traced

@trace
def foo(number, string, test):
    print("Het getal {0} schrijft men voluit als {1}. De variable {2} maakt niets uit...".format(number, string, test))

def main():
    foo(3, "drie", "test")

if __name__ == "__main__":
    # execute only if run as a script
    main()
